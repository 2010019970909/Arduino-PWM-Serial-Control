/*
   This program aims to control a PWM port using the Serial port.

   Author: Vincent STRAGIER
*/

const uint8_t PWM_PORT = 3;
String string_command = "";
// double command = 0.00;
uint8_t command = 0;

void setup() {
  Serial.begin(115200);
  while (!Serial);
  Serial.println("Setup is done.");
}

void loop() {
  while (Serial.available()) {
    string_command = Serial.readStringUntil('\n');
    // command = strtod(string_command.c_str(), (char **)NULL);
    command = string_command.toInt();
    analogWrite(PWM_PORT, command);
    Serial.println(command);
  }
}
