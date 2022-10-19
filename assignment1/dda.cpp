// Bresenham's Line Drawing
#include <GL/gl.h>
#include <GL/glut.h>
#include <stdio.h>

// Initialize the window
void myInit(int width, int height)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glClearColor(0.0, 0.0, 0.0, 1.0);
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(0, width, 0, height);
}

// Function to draw pixel
// void draw_pixel(int x, int y)
// {
//     glBegin(GL_POINTS);
//     glVertex2i(x, y);
//     glEnd();
// }

// void draw_line(int x1, int x2, int y1, int y2)
// {
//     int dx, dy, i, e;
//     int incx, incy, inc1, inc2;
//     int x, y;
//     dx = x2 - x1;
//     dy = y2 - y1;
//     if (dx < 0)
//         dx = -dx;
//     if (dy < 0)
//         dy = -dy;
//     incx = 1;
//     if (x2 < x1)
//         incx = -1;
//     incy = 1;
//     if (y2 < y1)
//         incy = -1;
//     x = x1;
//     y = y1;
//     if (dx > dy)
//     {
//         draw_pixel(x, y);
//         e = 2 * dy - dx;
//         inc1 = 2 * (dy - dx);
//         inc2 = 2 * dy;
//         for (i = 0; i < dx; i++)
//         {
//             if (e >= 0)
//             {
//                 y += incy;
//                 e += inc1;
//             }
//             else
//                 e += inc2;
//             x += incx;
//             draw_pixel(x, y);
//         }
//     }

//     else
//     {
//         draw_pixel(x, y);
//         e = 2 * dx - dy;
//         inc1 = 2 * (dx - dy);
//         inc2 = 2 * dx;
//         for (i = 0; i < dy; i++)
//         {
//             if (e >= 0)
//             {
//                 x += incx;
//                 e += inc1;
//             }
//             else
//                 e += inc2;
//             y += incy;
//             draw_pixel(x, y);
//         }
//     }
// }

// void myDisplay()
// {
//     // Should be implemented (The said algorithm)
//     draw_line(x1, x2, y1, y2);
//     glFlush();
// }

void initializeGLUT(int *argc, char **argv)
{
    glutInit(argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    int WINDOW_WIDTH, WINDOW_HEIGHT;
    char WINDOW_TITLE[500];
    printf("Give window height and width:\n");
    scanf("%d %d", &WINDOW_WIDTH, WINDOW_HEIGHT);
    printf("Give the name of the window:\n");
    scanf("%s", &WINDOW_TITLE);
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT);
    glutInitWindowPosition(0, 0);
    glutCreateWindow(WINDOW_TITLE);
    myInit(WINDOW_WIDTH, WINDOW_HEIGHT);
    // glutDisplayFunc(myDisplay);
    // glutMainLoop();
}

// int main(int argc, char **argv)
// {
//     glutInit(&argc, argv);
//     glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
//     int WINDOW_WIDTH, WINDOW_HEIGHT;
//     char WINDOW_TITLE[500];
//     printf("Give window height and width:\n");
//     scanf("%d %d", &WINDOW_WIDTH, WINDOW_HEIGHT);
//     printf("Give the name of the window:\n");
//     scanf("%s", &WINDOW_TITLE);
//     glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT);
//     glutInitWindowPosition(0, 0);
//     glutCreateWindow(WINDOW_TITLE);
//     myInit();
//     glutDisplayFunc(myDisplay);
//     glutMainLoop();

//     return 0;
// }
