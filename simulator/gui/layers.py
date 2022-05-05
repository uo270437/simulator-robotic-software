import drawing
import robot_drawings
import huds
import simulator.robots.robots as robots

class Layer:

    def __init__(self):
        """
        Constructor for superclass layer
        """
        self.drawing = drawing.Drawing()
        self.hud = None
        self.robot = None
        self.robot_drawing: robot_drawings.RobotDrawing = None
        self._zoom_percentage()
        self.is_drawing = False

    def execute(self):
        """
        Executes the code, showing what the robot will do on the canvas
        """
        self._drawing_config()
        self.robot_drawing.draw()
        self.is_drawing = True
        
    def stop(self):
        """
        Stops all the executing code and clears the canvas
        """
        self.drawing.empty_drawing()
        self.is_drawing = False

    def zoom_in(self):
        """
        Broadens the drawing
        """
        self.drawing.zoom_in()
        self._zoom_config()

    def zoom_out(self):
        """
        Unbroads the drawing
        """
        self.drawing.zoom_out()
        self._zoom_config()

    def move(self, using_keys, move_WASD, move_dir):
        """
        Moves the robot that is being used
        Arguments:
            using_keys: specifies keys are being used for movement (True)
            or not (False)
            move_WASD: a map that specifies if any of the keys WASD is being
            pressed
            move_dir: a map that specifies if arrow keys are being pressed
        """
        pass

    def set_canvas(self, canvas, hud_canvas):
        """
        Sets the canvas that the drawing and will use
        Arguments:
            canvas: the canvas of the drawing
            hud_canvas: the canvas of the hud
        """
        self.drawing.set_canvas(canvas)
        self.drawing.set_size(self.robot_drawing.drawing_width, self.robot_drawing.drawing_height)
        self.hud.set_canvas(hud_canvas)

    def _zoom_config(self):
        """
        Configures the zoom in case when it changes
        """
        self._zoom_percentage()
        if self.is_drawing:
            self._zoom_redraw()

    def _zoom_redraw(self):
        """
        Once the zoom changes, use this method for redrawing everything
        up to scale
        """
        self.drawing.delete_zoomables()
        self._draw_before_robot()
        self.robot_drawing.draw()

    def _draw_before_robot(self):
        pass

    def _zoom_percentage(self):
        """
        Updates the percentage of zoom that is being used currently
        """
        self.zoom_percent = self.drawing.zoom_percentage()

    def _drawing_config(self):
        """
        Method used to configure the drawing before executing
        """
        self.drawing.empty_drawing()


class MoblileRobotLayer(Layer):

    def __init__(self, n_light_sens):
        """
        Constructor for MobileRobotLayer
        """
        super().__init__()
        self.hud = huds.MobileHUD()
        self.robot = robots.MobileRobot(n_light_sens)
        self.robot_drawing = robot_drawings.MobileRobotDrawing(self.drawing, n_light_sens)
        self.circuit = robot_drawings.Circuit(self.drawing)
        self.obstacle = robot_drawings.Obstacle(700, 3000, 600, 450, self.drawing)

        self.is_rotating = False
        self.is_moving = False

    def move(self, using_keys, move_WASD, move_dir):
        """
        Move method of the layer. Moves the robot and rotates it
        """
        v = 0 #Velocity
        da = 0 #Angle
        if using_keys:
            v, da = self.__move_keys(move_WASD)
        else:
            v, da = self.__move_code()

        future_p = self.robot_drawing.predict_movement(v)
        if (
            v == 0 or
            future_p[0] <= self.robot_drawing.width / 2 or
            future_p[0] >= self.robot_drawing.drawing_width - self.robot_drawing.width / 2 or
            future_p[1] <= self.robot_drawing.height / 2 or
            future_p[1] >= self.robot_drawing.drawing_height - self.robot_drawing.height / 2 or
            self.__check_obstacle_collision(future_p[0], future_p[1])
        ):
            v = 0
            self.is_moving = False
        #Move or rotate
        self.__hud_velocity()
        if not self.is_rotating:
            self.robot_drawing.move(v)
        if not self.is_moving:
            self.robot_drawing.change_angle(da)

        #Overlapping check
        self.__check_circuit_overlap()  
        self.__detect_obstacle()

    def __move_keys(self, movement):
        """
        Moves the robot using WASD
        Arguments:
            movement: contains the information about the pressing
            of the keys
        """
        v = 0
        da = 0
        if not self.is_rotating:
            if movement["w"] == True:
                v = -10
            if movement["s"] == True:
                v = 10
            if v != 0:
                self.is_moving = True
            else:
                self.is_moving = False
        if not self.is_moving:
            if movement["a"] == True:
                da = 5
            if movement["d"] == True:
                da = -5
            if da != 0:
                self.is_rotating = True
            else:
                self.is_rotating = False
        return v, da

    def __move_code(self):
        """
        Moves the robot using the programmed instructions
        """
        v = 0
        da = 0
        #self.robot.servo_left.value = 0
        #self.robot.servo_right.value = 0
        v_i = int((self.robot.servo_left.get_value() - 90) / 10)
        v_r = int((self.robot.servo_right.get_value() - 90) / 10)
        rotates = False
        if v_i >= 0 and v_r >= 0:
            if v_i != 0 or v_r != 0:
                da = -5
                rotates = True
        if v_i <= 0 and v_r <= 0:
            if v_i != 0 or v_r != 0:
                da = 5
                rotates = True
        if abs(v_i) == abs(v_r) and not rotates:
            if v_i > 0:
                v = -v_i
            if v_i < 0:
                v = -v_i
        return v, da

    def _drawing_config(self):
        """
        Configures the drawing before executing or after
        updating
        """
        super()._drawing_config()
        self.__create_circuit()
        self.__create_obstacle()

    def _draw_before_robot(self):
        """
        Draws before the robot so the z-index is correct
        """
        self.__create_circuit()
        self.__create_obstacle()

    def __create_circuit(self):
        """
        Creates and draws the circuit in the canvas
        """
        self.circuit.create_circuit()

    def __create_obstacle(self):
        """
        Draws the obstacle in the canvas
        """
        self.obstacle.draw()

    def __check_circuit_overlap(self):
        """
        Checks if the robot is inside or outside of the circuit
        """
        measurements = []
        values = []
        for sens in self.robot_drawing.sensors["light"]:
            x = sens.x
            y = sens.y
            if self.circuit.is_overlapping(x, y):
                sens.dark()
                measurements.append(True)
                values.append(1)
            else:
                sens.light()
                measurements.append(False)
                values.append(0)
        self.robot.set_light_sens_value(values)
        self.robot_drawing.repaint_light_sensors()
        self.hud.set_circuit(measurements)

    def __check_obstacle_collision(self, x, y):
        """
        Checks if the robot collides with the obstacle
        Arguments:
            x: the expected x position
            y: the expected y position
        Returns:
            True if collides, False if else
        """
        return (
            x + self.robot_drawing.width / 2 >= self.obstacle.x and
            y + self.robot_drawing.height / 2 >= self.obstacle.y and
            x <= self.obstacle.x + (self.obstacle.width + self.robot_drawing.width / 2) and
            y <= self.obstacle.y + (self.obstacle.height + self.robot_drawing.height / 2) 
        )

    def __detect_obstacle(self):
        """
        Checks for every ultrasound sensor if it detects
        any obstacle in front of it, and then sends the data
        to the hud, so it can be parsed
        """
        dists = []
        dists.append(self.obstacle.calculate_distance(self.robot_drawing.sensors["sound"].x, self.robot_drawing.sensors["sound"].y, self.robot_drawing.angle))
        if dists[-1] != -1:
            self.robot_drawing.sensors["sound"].set_detect(True)
            self.robot.sound.value = 1
            self.robot.sound.dist = dists[-1]
        else:
            self.robot_drawing.sensors["sound"].set_detect(False)
            self.robot.sound.value = 0
            self.robot.sound.dist = -1
        self.hud.set_detect_obstacle(dists)

    def __hud_velocity(self):
        """
        Sends the velocity data of the wheels to the hud,
        so it can be parsed
        """
        self.hud.set_wheel([self.robot_drawing.vl, self.robot_drawing.vr])

class LinearActuatorLayer(Layer):

    def __init__(self):
        """
        Constuctor for LinearActuatorLayer
        """
        super().__init__()
        self.hud = huds.ActuatorHUD()
        self.robot = robots.LinearActuator()
        self.robot_drawing = robot_drawings.LinearActuatorDrawing(self.drawing)

    def move(self, using_keys, move_WASD, move_dir):
        """
        Move method of the layer. Moves the block of the
        linear actuator
        """
        v = 0
        self.robot_drawing.hit = False
        if using_keys:
            v = self.__move_keys(move_WASD)
        else:
            self.__parse_joystick(move_dir)
            v = self.__move_code()
        self.robot_drawing.move(v)
        self.hud.set_direction(v * 25)
        self.hud.set_pressed([self.robot_drawing.but_left.pressed, self.robot_drawing.but_right.pressed])

    def __move_keys(self, movement):
        """
        Moves the robot using WASD
        Arguments:
            movement: contains the information about the pressing
            of the keys
        """
        v = 0
        if movement["a"] == True:
            if self.robot_drawing.block.x > 508:
                v -= 10
            self.__hit_left(v == 0)
        elif movement["d"] == True:
            if self.robot_drawing.block.x < 1912:
                v += 10
            self.__hit_right(v == 0)
        return v

    def __move_code(self):
        """
        Moves the robot using the programmed instructions
        """
        v = 0
        #self.robot.servo.value = 0
        v_s = int((self.robot.servo.value - 90) / 10)
        if v_s > 0:
            if self.robot_drawing.block.x < 1912:
                v = v_s
            self.__hit_right(v == 0)
        if v_s < 0:
            if self.robot_drawing.block.x > 508:
                v = v_s
            self.__hit_left(v == 0)
        return v

    def __parse_joystick(self, movement):
        """
        The direction keys will be used as joystick.
        This method will parse the value of the joystick
        knowing what direction keys are being pressed.
        Arguments:
            movement: a map with the direction keys and if
            they are being pressed or not
        """
        dx = 500
        dy = 500
        if movement["up"] == True:
            dy = 0
        if movement["down"] == True:
            dy = 1023
        if movement["left"] == True:
            dx = 0
        if movement["right"] == True:
            dx = 1023
        #print("diff x: {}, diff y: {}".format(dx, dy))
        self.robot.joystick.dx = dx
        self.robot.joystick.dy = dy

    def __hit_left(self, has_hit):
        """
        Establishes the value for the left button
        Arguments:
            has_hit: True if the button has been hit, False
            if else
        """
        if has_hit:
            self.robot_drawing.hit = True
            self.robot.button_left.value = 1
        else:
            self.robot_drawing.hit = False
            self.robot.button_left.value = 0

    def __hit_right(self, has_hit):
        """
        Establishes the value for the right button
        Arguments:
            has_hit: True if the button has been hit, False
            if else
        """
        if has_hit:
            self.robot_drawing.hit = True
            self.robot.button_right.value = 1
        else:
            self.robot_drawing.hit = False
            self.robot.button_right.value = 0