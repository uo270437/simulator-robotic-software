# Generated from E:\Asignaturas\Cuarto\TFG\SimuladorSoftwareRobots\simulator\compiler\Arduino.g4 by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,87,595,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,
        10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,
        17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,
        19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,
        21,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,
        28,1,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,
        32,1,32,1,32,1,32,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,35,1,35,1,
        35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,
        38,1,38,1,38,1,38,1,38,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,
        40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,
        42,1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,
        44,1,44,1,44,1,45,1,45,1,45,1,45,1,45,1,45,1,46,1,46,1,46,1,47,1,
        47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,53,1,
        53,1,54,1,54,1,55,1,55,1,55,1,56,1,56,1,56,1,57,1,57,1,57,1,58,1,
        58,1,58,1,59,1,59,1,60,1,60,1,61,1,61,1,62,1,62,1,62,1,63,1,63,1,
        63,1,64,1,64,1,64,1,65,1,65,1,65,1,66,1,66,1,66,1,67,1,67,1,67,1,
        68,1,68,1,68,1,69,1,69,1,69,1,70,1,70,1,70,1,71,1,71,1,71,1,72,1,
        72,1,72,1,73,1,73,1,73,1,74,1,74,1,74,4,74,499,8,74,11,74,12,74,
        500,1,75,1,75,4,75,505,8,75,11,75,12,75,506,1,76,1,76,1,76,4,76,
        512,8,76,11,76,12,76,513,1,77,3,77,517,8,77,1,77,4,77,520,8,77,11,
        77,12,77,521,1,78,3,78,525,8,78,1,78,4,78,528,8,78,11,78,12,78,529,
        1,78,1,78,4,78,534,8,78,11,78,12,78,535,1,79,1,79,1,79,1,80,1,80,
        1,80,1,81,1,81,1,81,1,82,1,82,5,82,549,8,82,10,82,12,82,552,9,82,
        1,83,1,83,5,83,556,8,83,10,83,12,83,559,9,83,1,84,1,84,1,84,1,84,
        5,84,565,8,84,10,84,12,84,568,9,84,1,84,3,84,571,8,84,1,84,1,84,
        1,85,1,85,1,85,1,85,5,85,579,8,85,10,85,12,85,582,9,85,1,85,1,85,
        1,85,1,85,1,85,1,86,4,86,590,8,86,11,86,12,86,591,1,86,1,86,2,566,
        580,0,87,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,
        23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,
        34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,
        45,91,46,93,47,95,48,97,49,99,50,101,51,103,52,105,53,107,54,109,
        55,111,56,113,57,115,58,117,59,119,60,121,61,123,62,125,63,127,64,
        129,65,131,66,133,67,135,68,137,69,139,70,141,71,143,72,145,73,147,
        74,149,75,151,76,153,77,155,78,157,79,159,80,161,81,163,82,165,83,
        167,84,169,85,171,86,173,87,1,0,10,1,0,48,49,1,0,48,55,3,0,48,57,
        65,70,97,102,1,0,48,57,3,0,10,10,39,39,92,92,3,0,10,10,34,34,92,
        92,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,1,1,10,10,
        3,0,9,10,13,13,32,32,607,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,
        1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,
        1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,
        1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,
        1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,
        1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,
        1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,
        1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,
        1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,
        1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,
        107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,
        0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,
        1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,
        0,135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,141,1,0,0,0,0,143,1,
        0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,1,0,0,0,0,151,1,0,0,0,0,
        153,1,0,0,0,0,155,1,0,0,0,0,157,1,0,0,0,0,159,1,0,0,0,0,161,1,0,
        0,0,0,163,1,0,0,0,0,165,1,0,0,0,0,167,1,0,0,0,0,169,1,0,0,0,0,171,
        1,0,0,0,0,173,1,0,0,0,1,175,1,0,0,0,3,184,1,0,0,0,5,186,1,0,0,0,
        7,188,1,0,0,0,9,190,1,0,0,0,11,192,1,0,0,0,13,198,1,0,0,0,15,205,
        1,0,0,0,17,207,1,0,0,0,19,215,1,0,0,0,21,217,1,0,0,0,23,219,1,0,
        0,0,25,221,1,0,0,0,27,223,1,0,0,0,29,225,1,0,0,0,31,230,1,0,0,0,
        33,238,1,0,0,0,35,243,1,0,0,0,37,248,1,0,0,0,39,255,1,0,0,0,41,261,
        1,0,0,0,43,265,1,0,0,0,45,270,1,0,0,0,47,276,1,0,0,0,49,283,1,0,
        0,0,51,290,1,0,0,0,53,303,1,0,0,0,55,317,1,0,0,0,57,331,1,0,0,0,
        59,336,1,0,0,0,61,341,1,0,0,0,63,343,1,0,0,0,65,345,1,0,0,0,67,351,
        1,0,0,0,69,354,1,0,0,0,71,358,1,0,0,0,73,361,1,0,0,0,75,366,1,0,
        0,0,77,373,1,0,0,0,79,378,1,0,0,0,81,380,1,0,0,0,83,388,1,0,0,0,
        85,395,1,0,0,0,87,401,1,0,0,0,89,410,1,0,0,0,91,415,1,0,0,0,93,421,
        1,0,0,0,95,424,1,0,0,0,97,427,1,0,0,0,99,429,1,0,0,0,101,431,1,0,
        0,0,103,433,1,0,0,0,105,435,1,0,0,0,107,437,1,0,0,0,109,439,1,0,
        0,0,111,441,1,0,0,0,113,444,1,0,0,0,115,447,1,0,0,0,117,450,1,0,
        0,0,119,453,1,0,0,0,121,455,1,0,0,0,123,457,1,0,0,0,125,459,1,0,
        0,0,127,462,1,0,0,0,129,465,1,0,0,0,131,468,1,0,0,0,133,471,1,0,
        0,0,135,474,1,0,0,0,137,477,1,0,0,0,139,480,1,0,0,0,141,483,1,0,
        0,0,143,486,1,0,0,0,145,489,1,0,0,0,147,492,1,0,0,0,149,495,1,0,
        0,0,151,502,1,0,0,0,153,508,1,0,0,0,155,516,1,0,0,0,157,524,1,0,
        0,0,159,537,1,0,0,0,161,540,1,0,0,0,163,543,1,0,0,0,165,546,1,0,
        0,0,167,553,1,0,0,0,169,560,1,0,0,0,171,574,1,0,0,0,173,589,1,0,
        0,0,175,176,5,35,0,0,176,177,5,105,0,0,177,178,5,110,0,0,178,179,
        5,99,0,0,179,180,5,108,0,0,180,181,5,117,0,0,181,182,5,100,0,0,182,
        183,5,101,0,0,183,2,1,0,0,0,184,185,5,60,0,0,185,4,1,0,0,0,186,187,
        5,46,0,0,187,6,1,0,0,0,188,189,5,62,0,0,189,8,1,0,0,0,190,191,5,
        59,0,0,191,10,1,0,0,0,192,193,5,99,0,0,193,194,5,111,0,0,194,195,
        5,110,0,0,195,196,5,115,0,0,196,197,5,116,0,0,197,12,1,0,0,0,198,
        199,5,115,0,0,199,200,5,116,0,0,200,201,5,97,0,0,201,202,5,116,0,
        0,202,203,5,105,0,0,203,204,5,99,0,0,204,14,1,0,0,0,205,206,5,61,
        0,0,206,16,1,0,0,0,207,208,5,35,0,0,208,209,5,100,0,0,209,210,5,
        101,0,0,210,211,5,102,0,0,211,212,5,105,0,0,212,213,5,110,0,0,213,
        214,5,101,0,0,214,18,1,0,0,0,215,216,5,91,0,0,216,20,1,0,0,0,217,
        218,5,93,0,0,218,22,1,0,0,0,219,220,5,123,0,0,220,24,1,0,0,0,221,
        222,5,44,0,0,222,26,1,0,0,0,223,224,5,125,0,0,224,28,1,0,0,0,225,
        226,5,98,0,0,226,227,5,111,0,0,227,228,5,111,0,0,228,229,5,108,0,
        0,229,30,1,0,0,0,230,231,5,98,0,0,231,232,5,111,0,0,232,233,5,111,
        0,0,233,234,5,108,0,0,234,235,5,101,0,0,235,236,5,97,0,0,236,237,
        5,110,0,0,237,32,1,0,0,0,238,239,5,98,0,0,239,240,5,121,0,0,240,
        241,5,116,0,0,241,242,5,101,0,0,242,34,1,0,0,0,243,244,5,99,0,0,
        244,245,5,104,0,0,245,246,5,97,0,0,246,247,5,114,0,0,247,36,1,0,
        0,0,248,249,5,100,0,0,249,250,5,111,0,0,250,251,5,117,0,0,251,252,
        5,98,0,0,252,253,5,108,0,0,253,254,5,101,0,0,254,38,1,0,0,0,255,
        256,5,102,0,0,256,257,5,108,0,0,257,258,5,111,0,0,258,259,5,97,0,
        0,259,260,5,116,0,0,260,40,1,0,0,0,261,262,5,105,0,0,262,263,5,110,
        0,0,263,264,5,116,0,0,264,42,1,0,0,0,265,266,5,108,0,0,266,267,5,
        111,0,0,267,268,5,110,0,0,268,269,5,103,0,0,269,44,1,0,0,0,270,271,
        5,115,0,0,271,272,5,104,0,0,272,273,5,111,0,0,273,274,5,114,0,0,
        274,275,5,116,0,0,275,46,1,0,0,0,276,277,5,115,0,0,277,278,5,105,
        0,0,278,279,5,122,0,0,279,280,5,101,0,0,280,281,5,95,0,0,281,282,
        5,116,0,0,282,48,1,0,0,0,283,284,5,83,0,0,284,285,5,116,0,0,285,
        286,5,114,0,0,286,287,5,105,0,0,287,288,5,110,0,0,288,289,5,103,
        0,0,289,50,1,0,0,0,290,291,5,117,0,0,291,292,5,110,0,0,292,293,5,
        115,0,0,293,294,5,105,0,0,294,295,5,103,0,0,295,296,5,110,0,0,296,
        297,5,101,0,0,297,298,5,100,0,0,298,299,5,32,0,0,299,300,5,105,0,
        0,300,301,5,110,0,0,301,302,5,116,0,0,302,52,1,0,0,0,303,304,5,117,
        0,0,304,305,5,110,0,0,305,306,5,115,0,0,306,307,5,105,0,0,307,308,
        5,103,0,0,308,309,5,110,0,0,309,310,5,101,0,0,310,311,5,100,0,0,
        311,312,5,32,0,0,312,313,5,99,0,0,313,314,5,104,0,0,314,315,5,97,
        0,0,315,316,5,114,0,0,316,54,1,0,0,0,317,318,5,117,0,0,318,319,5,
        110,0,0,319,320,5,115,0,0,320,321,5,105,0,0,321,322,5,103,0,0,322,
        323,5,110,0,0,323,324,5,101,0,0,324,325,5,100,0,0,325,326,5,32,0,
        0,326,327,5,108,0,0,327,328,5,111,0,0,328,329,5,110,0,0,329,330,
        5,103,0,0,330,56,1,0,0,0,331,332,5,118,0,0,332,333,5,111,0,0,333,
        334,5,105,0,0,334,335,5,100,0,0,335,58,1,0,0,0,336,337,5,119,0,0,
        337,338,5,111,0,0,338,339,5,114,0,0,339,340,5,100,0,0,340,60,1,0,
        0,0,341,342,5,40,0,0,342,62,1,0,0,0,343,344,5,41,0,0,344,64,1,0,
        0,0,345,346,5,119,0,0,346,347,5,104,0,0,347,348,5,105,0,0,348,349,
        5,108,0,0,349,350,5,101,0,0,350,66,1,0,0,0,351,352,5,100,0,0,352,
        353,5,111,0,0,353,68,1,0,0,0,354,355,5,102,0,0,355,356,5,111,0,0,
        356,357,5,114,0,0,357,70,1,0,0,0,358,359,5,105,0,0,359,360,5,102,
        0,0,360,72,1,0,0,0,361,362,5,101,0,0,362,363,5,108,0,0,363,364,5,
        115,0,0,364,365,5,101,0,0,365,74,1,0,0,0,366,367,5,115,0,0,367,368,
        5,119,0,0,368,369,5,105,0,0,369,370,5,116,0,0,370,371,5,99,0,0,371,
        372,5,104,0,0,372,76,1,0,0,0,373,374,5,99,0,0,374,375,5,97,0,0,375,
        376,5,115,0,0,376,377,5,101,0,0,377,78,1,0,0,0,378,379,5,58,0,0,
        379,80,1,0,0,0,380,381,5,100,0,0,381,382,5,101,0,0,382,383,5,102,
        0,0,383,384,5,97,0,0,384,385,5,117,0,0,385,386,5,108,0,0,386,387,
        5,116,0,0,387,82,1,0,0,0,388,389,5,114,0,0,389,390,5,101,0,0,390,
        391,5,116,0,0,391,392,5,117,0,0,392,393,5,114,0,0,393,394,5,110,
        0,0,394,84,1,0,0,0,395,396,5,98,0,0,396,397,5,114,0,0,397,398,5,
        101,0,0,398,399,5,97,0,0,399,400,5,107,0,0,400,86,1,0,0,0,401,402,
        5,99,0,0,402,403,5,111,0,0,403,404,5,110,0,0,404,405,5,116,0,0,405,
        406,5,105,0,0,406,407,5,110,0,0,407,408,5,117,0,0,408,409,5,101,
        0,0,409,88,1,0,0,0,410,411,5,116,0,0,411,412,5,114,0,0,412,413,5,
        117,0,0,413,414,5,101,0,0,414,90,1,0,0,0,415,416,5,102,0,0,416,417,
        5,97,0,0,417,418,5,108,0,0,418,419,5,115,0,0,419,420,5,101,0,0,420,
        92,1,0,0,0,421,422,5,43,0,0,422,423,5,43,0,0,423,94,1,0,0,0,424,
        425,5,45,0,0,425,426,5,45,0,0,426,96,1,0,0,0,427,428,5,33,0,0,428,
        98,1,0,0,0,429,430,5,126,0,0,430,100,1,0,0,0,431,432,5,42,0,0,432,
        102,1,0,0,0,433,434,5,47,0,0,434,104,1,0,0,0,435,436,5,37,0,0,436,
        106,1,0,0,0,437,438,5,43,0,0,438,108,1,0,0,0,439,440,5,45,0,0,440,
        110,1,0,0,0,441,442,5,62,0,0,442,443,5,61,0,0,443,112,1,0,0,0,444,
        445,5,60,0,0,445,446,5,61,0,0,446,114,1,0,0,0,447,448,5,61,0,0,448,
        449,5,61,0,0,449,116,1,0,0,0,450,451,5,33,0,0,451,452,5,61,0,0,452,
        118,1,0,0,0,453,454,5,38,0,0,454,120,1,0,0,0,455,456,5,94,0,0,456,
        122,1,0,0,0,457,458,5,124,0,0,458,124,1,0,0,0,459,460,5,38,0,0,460,
        461,5,38,0,0,461,126,1,0,0,0,462,463,5,124,0,0,463,464,5,124,0,0,
        464,128,1,0,0,0,465,466,5,37,0,0,466,467,5,61,0,0,467,130,1,0,0,
        0,468,469,5,38,0,0,469,470,5,61,0,0,470,132,1,0,0,0,471,472,5,42,
        0,0,472,473,5,61,0,0,473,134,1,0,0,0,474,475,5,43,0,0,475,476,5,
        61,0,0,476,136,1,0,0,0,477,478,5,45,0,0,478,479,5,61,0,0,479,138,
        1,0,0,0,480,481,5,47,0,0,481,482,5,61,0,0,482,140,1,0,0,0,483,484,
        5,94,0,0,484,485,5,61,0,0,485,142,1,0,0,0,486,487,5,124,0,0,487,
        488,5,61,0,0,488,144,1,0,0,0,489,490,5,60,0,0,490,491,5,60,0,0,491,
        146,1,0,0,0,492,493,5,62,0,0,493,494,5,62,0,0,494,148,1,0,0,0,495,
        496,5,48,0,0,496,498,5,98,0,0,497,499,7,0,0,0,498,497,1,0,0,0,499,
        500,1,0,0,0,500,498,1,0,0,0,500,501,1,0,0,0,501,150,1,0,0,0,502,
        504,5,48,0,0,503,505,7,1,0,0,504,503,1,0,0,0,505,506,1,0,0,0,506,
        504,1,0,0,0,506,507,1,0,0,0,507,152,1,0,0,0,508,509,5,48,0,0,509,
        511,5,120,0,0,510,512,7,2,0,0,511,510,1,0,0,0,512,513,1,0,0,0,513,
        511,1,0,0,0,513,514,1,0,0,0,514,154,1,0,0,0,515,517,5,45,0,0,516,
        515,1,0,0,0,516,517,1,0,0,0,517,519,1,0,0,0,518,520,7,3,0,0,519,
        518,1,0,0,0,520,521,1,0,0,0,521,519,1,0,0,0,521,522,1,0,0,0,522,
        156,1,0,0,0,523,525,5,45,0,0,524,523,1,0,0,0,524,525,1,0,0,0,525,
        527,1,0,0,0,526,528,7,3,0,0,527,526,1,0,0,0,528,529,1,0,0,0,529,
        527,1,0,0,0,529,530,1,0,0,0,530,531,1,0,0,0,531,533,5,46,0,0,532,
        534,7,3,0,0,533,532,1,0,0,0,534,535,1,0,0,0,535,533,1,0,0,0,535,
        536,1,0,0,0,536,158,1,0,0,0,537,538,3,161,80,0,538,539,5,39,0,0,
        539,160,1,0,0,0,540,541,5,39,0,0,541,542,8,4,0,0,542,162,1,0,0,0,
        543,544,3,165,82,0,544,545,5,34,0,0,545,164,1,0,0,0,546,550,5,34,
        0,0,547,549,8,5,0,0,548,547,1,0,0,0,549,552,1,0,0,0,550,548,1,0,
        0,0,550,551,1,0,0,0,551,166,1,0,0,0,552,550,1,0,0,0,553,557,7,6,
        0,0,554,556,7,7,0,0,555,554,1,0,0,0,556,559,1,0,0,0,557,555,1,0,
        0,0,557,558,1,0,0,0,558,168,1,0,0,0,559,557,1,0,0,0,560,561,5,47,
        0,0,561,562,5,47,0,0,562,566,1,0,0,0,563,565,9,0,0,0,564,563,1,0,
        0,0,565,568,1,0,0,0,566,567,1,0,0,0,566,564,1,0,0,0,567,570,1,0,
        0,0,568,566,1,0,0,0,569,571,7,8,0,0,570,569,1,0,0,0,571,572,1,0,
        0,0,572,573,6,84,0,0,573,170,1,0,0,0,574,575,5,47,0,0,575,576,5,
        42,0,0,576,580,1,0,0,0,577,579,9,0,0,0,578,577,1,0,0,0,579,582,1,
        0,0,0,580,581,1,0,0,0,580,578,1,0,0,0,581,583,1,0,0,0,582,580,1,
        0,0,0,583,584,5,42,0,0,584,585,5,47,0,0,585,586,1,0,0,0,586,587,
        6,85,0,0,587,172,1,0,0,0,588,590,7,9,0,0,589,588,1,0,0,0,590,591,
        1,0,0,0,591,589,1,0,0,0,591,592,1,0,0,0,592,593,1,0,0,0,593,594,
        6,86,0,0,594,174,1,0,0,0,15,0,500,506,513,516,521,524,529,535,550,
        557,566,570,580,591,1,6,0,0
    ]

class ArduinoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    T__53 = 54
    T__54 = 55
    T__55 = 56
    T__56 = 57
    T__57 = 58
    T__58 = 59
    T__59 = 60
    T__60 = 61
    T__61 = 62
    T__62 = 63
    T__63 = 64
    T__64 = 65
    T__65 = 66
    T__66 = 67
    T__67 = 68
    T__68 = 69
    T__69 = 70
    T__70 = 71
    T__71 = 72
    BIT_SHIFT_L = 73
    BIT_SHIFT_R = 74
    BINARY_CONST = 75
    OCTAL_CONST = 76
    HEX_CONST = 77
    INT_CONST = 78
    FLOAT_CONST = 79
    CHAR_CONST = 80
    UNTERMINATED_CHAR = 81
    STRING_CONST = 82
    UNTERMINATED_STRING = 83
    ID = 84
    LINE_COMMENT = 85
    MULTILINE_COMMENT = 86
    WHITESPACE = 87

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'#include'", "'<'", "'.'", "'>'", "';'", "'const'", "'static'", 
            "'='", "'#define'", "'['", "']'", "'{'", "','", "'}'", "'bool'", 
            "'boolean'", "'byte'", "'char'", "'double'", "'float'", "'int'", 
            "'long'", "'short'", "'size_t'", "'String'", "'unsigned int'", 
            "'unsigned char'", "'unsigned long'", "'void'", "'word'", "'('", 
            "')'", "'while'", "'do'", "'for'", "'if'", "'else'", "'switch'", 
            "'case'", "':'", "'default'", "'return'", "'break'", "'continue'", 
            "'true'", "'false'", "'++'", "'--'", "'!'", "'~'", "'*'", "'/'", 
            "'%'", "'+'", "'-'", "'>='", "'<='", "'=='", "'!='", "'&'", 
            "'^'", "'|'", "'&&'", "'||'", "'%='", "'&='", "'*='", "'+='", 
            "'-='", "'/='", "'^='", "'|='" ]

    symbolicNames = [ "<INVALID>",
            "BIT_SHIFT_L", "BIT_SHIFT_R", "BINARY_CONST", "OCTAL_CONST", 
            "HEX_CONST", "INT_CONST", "FLOAT_CONST", "CHAR_CONST", "UNTERMINATED_CHAR", 
            "STRING_CONST", "UNTERMINATED_STRING", "ID", "LINE_COMMENT", 
            "MULTILINE_COMMENT", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "T__46", "T__47", "T__48", "T__49", 
                  "T__50", "T__51", "T__52", "T__53", "T__54", "T__55", 
                  "T__56", "T__57", "T__58", "T__59", "T__60", "T__61", 
                  "T__62", "T__63", "T__64", "T__65", "T__66", "T__67", 
                  "T__68", "T__69", "T__70", "T__71", "BIT_SHIFT_L", "BIT_SHIFT_R", 
                  "BINARY_CONST", "OCTAL_CONST", "HEX_CONST", "INT_CONST", 
                  "FLOAT_CONST", "CHAR_CONST", "UNTERMINATED_CHAR", "STRING_CONST", 
                  "UNTERMINATED_STRING", "ID", "LINE_COMMENT", "MULTILINE_COMMENT", 
                  "WHITESPACE" ]

    grammarFileName = "Arduino.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


