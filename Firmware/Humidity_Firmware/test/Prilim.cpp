#include "DHT.h"

// Define which pin the DATA pin of the DHT22 is connected to
#define DHTPIN 2     

// Define the type of sensor you are using
#define DHTTYPE DHT22   

// Initialize the DHT sensor
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // Start the serial communication
  Serial.begin(115200);
  Serial.println("DHT22 Preliminary Test Initiated!");

  // Initialize the DHT22 sensor
  dht.begin();
}

void loop() {
  // Wait 2 seconds between measurements (DHT22 is a bit slow)
  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds!
  float humidity = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float temperature = dht.readTemperature();

  // Check if any reads failed and exit early (to try again).
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor! Check your wiring.");
    return;
  }

  // Print the results to the Serial Monitor
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print("%  |  ");
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println("°C");
}