#include <IRLibAll.h>

// Define button pushes
#define KEY_OK 0x20DF22DD
#define KEY_EXIT 0x20DFDA25
#define KEY_UP 0x20DF02FD
#define KEY_DOWN 0x20DF827D
#define KEY_VOLUMEDOWN 0x20DFC03F
#define KEY_VOLUMEUP 0x20DF40BF
#define KEY_SOURCE 0x20DFD02F
#define KEY_POWER 0x20DF10EF
#define KEY_MUTE 0x20DF906F
 
IRsendNEC mySender;
 
void setup() {
  Serial.begin(9600);
}
 
void loop() {
  if (Serial.read() != -1) {
    //send a code every time a character is received from the serial port
    //Sony DVD power A8BCA
    mySender.send(KEY_POWER);
  }
}
