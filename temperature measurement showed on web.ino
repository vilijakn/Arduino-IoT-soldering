#include <ESP8266WiFi.h>
const char* ssid = "ssid";
const char* password = "password";
WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status()!=WL_CONNECTED){
    delay(500);
  }
  server.begin();
  Serial.println(WiFi.localIP());
}

void loop() {
  int sensorValue=analogRead(A0);
  float voltage = sensorValue * (3.1 /1023);
  int temperature = sensorValue*150/1024-25;
  Serial.println("Temperature");
  Serial.println(temperature);
  WiFiClient client = server.available();
client.println("HTTP/1.1 200 OK");
client.println("Content-Type: text/html");
client.println("Connection: close");
client.println("Refresh: 10");
client.println();
client.println("<!DOCTYPE HTML>");
client.println("<html>");
client.print("<p style='text-align: center;'><span style='color: #0000ff;'><strong style='font-size: large;'>Temperature = ");
client.print(temperature);
client.println("C");
client.print("</p>");
client.println("</html>");
delay(500);
}
