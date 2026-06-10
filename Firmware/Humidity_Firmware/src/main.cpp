#include "DHT.h"
#define DHTPIN 4  
#define DHTTYPE DHT22   
DHT dht(DHTPIN, DHTTYPE);

float avg_humidity = 0.0;
float avg_temperature = 0.0;
int count = 0;

void setup() {
  Serial.begin(115200);
  Serial.println("DHT22 Sensor Data");

  dht.begin();
}

void loop() {
  delay(500);

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor");
    return;
  }

  else{
    count++;
    avg_humidity = ((avg_humidity * (count - 1)) + humidity) / count;
    avg_temperature = ((avg_temperature * (count - 1)) + temperature) / count;
  }

  Serial.print("Relative Humidity: ");
  Serial.print(avg_humidity);
  Serial.print("%  |  ");
  Serial.print("Temperature: ");
  Serial.print(avg_temperature);
  Serial.println("°C");
} 