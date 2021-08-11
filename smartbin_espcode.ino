/* 
Author  : Himanshu Raj 
Date    : 08-07-2021
E-mail  : himanshuraj9194@gmail.com

Contiributed to Project : IoT Based Smart Dustbin 
*/
// Libraries 
  #include <ESP8266WiFi.h>
  #include "Adafruit_MQTT.h"
  #include "Adafruit_MQTT_Client.h"
/*___________________________________________________________________________________
----------------------WiFi Credentials---------------------------------------------*/
  #define WLAN_SSID      "iot"            // WiFi SSID(service set identifier)
  #define WLAN_PASSWORD  "project1234"    // WiFi Password
/*___________________________________________________________________________________
----------------------Adafruit IO Credentials--------------------------------------*/
  #define AIO_SERVER       "io.adafruit.com"
  #define AIO_SERVERPORT    1883
  #define AIO_USERNAME     "Himanshu00"
  #define AIO_KEY          "aio_PvRN12PEyIWDGjYiOD6aPqvYG2rY"
/* _________________________________________________________________________________
-----------------------Variables---------------------------------------------------*/
  #define  BIN_ID = "sd01"          //( Unique For each IoT Device Used in define Publish Object )
  const int Max_depth= 300;        //(in CM )
  int Curr_depth;                 //(in CM )
  const int trigPin = 3;
  const int echoPin = 2;
  long duration;
  int Ptg_full;
/* _________________________________________________________________________________
------------------------Setup the MQTT client class-------------------------------*/
//Setup the MQTT client class by passing in the WiFi client and MQTT server and login details.
  WiFiClient client;
  Adafruit_MQTT_Client mqtt(&client, AIO_SERVER, AIO_SERVERPORT, AIO_USERNAME, AIO_KEY);
  Adafruit_MQTT_Publish BIN_Data= Adafruit_MQTT_Publish(&mqtt, AIO_USERNAME "/feeds/sd01");


void setup() 
{
  Serial.begin(115200);
  pinMode(LED_BUILTIN,OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

}

void loop() 
{
/*_____________________________________________________________________________________
-----------------------Reading Ultrasonic Sensor Data & Mapping ---------------------*/
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  Curr_depth = duration * 0.0340 / 2;
  
  Serial.println("current Depth of Dustbin = ");
  Serial.print(Curr_depth);
  Serial.println(" ");

  Ptg_full=(Curr_depth*100)/Max_depth;

  Serial.println("Percentage Full =");
  Serial.print(Ptg_full);
  Serial.println(" ");

  
  
/*_________________________________________________________________________________
-----------------------Establishing Connection to WiFi---------------------------*/
   WiFi.begin(WLAN_SSID, WLAN_PASSWORD);
   while (WiFi.status() != WL_CONNECTED) 
    {
      delay(500);
      Serial.print(".");
    }
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.print(WiFi.localIP());
  Serial.println("");
  digitalWrite(LED_BUILTIN,LOW);   // Turn On ON board LED (Active Low)
/*__________________________________________________________________________________
-----------------------Establishing Connection to Adafruit IO --------------------*/

  Reconnect :                           // goto tag for reconnection to Adafruit IO
  Serial.println("Connecting to Adafruit IO...... ");
  int8_t ret;
  while ((ret = mqtt.connect()) != 0) 
    {
      switch (ret) 
        {
          case 1: Serial.println(F("Wrong protocol")); break;
          case 2: Serial.println(F("ID rejected")); break;
          case 3: Serial.println(F("Server unavail")); break;
          case 4: Serial.println(F("Bad user/pass")); break;
          case 5: Serial.println(F("Not authed")); break;
          case 6: Serial.println(F("Failed to subscribe")); break;
          default: Serial.println(F("Connection failed")); break;
        }

      if (ret >= 0)
        mqtt.disconnect();

      Serial.println(F("Retrying connection..."));
      delay(10000);
    }
  Serial.println(F("Adafruit IO Connected !"));



//_____________________________________________________________________________________
// -----------------------Publishing data to  Adafruit IO -----------------------------

  if (! BIN_Data.publish(percentage_full)) 
    {                    
      Serial.println(F("Failed"));
    }

  else
  {
    Serial.println(F("Published  !"));
  }

//_____________________________________________________________________________________
// -----------------------Going to Deep Sleep  ----------------------------------------

delay(5000);

ESP.deepSleep(9e8);


/*_____________________________________________________________________________________
-----------------------Reading Sensor Data -------------------------------------------
  current_depth_of_dustbin = random(300);

      // using ultrasonic sensor ;
  Serial.println("current depth_of_dustbin");
  Serial.print(current_depth_of_dustbin);
  Serial.println(" ");

//_____________________________________________________________________________________
// -----------------------Mapping  Sensor Data ----------------------------------------
  int percentage_full  =map(current_depth_of_dustbin,0,Max_depth_of_dustbin,0,100);
  Serial.println("Dustbin is :  ");
  Serial.print(percentage_full);
  Serial.print(" % Full ");
//____________________________________________________________________________________
// -----------------------Pinging Adafruit IO ----------------------------------------
// ping adafruit io a few times to make sure we remain connected
  if (! mqtt.ping(3)) 
    {
      // reconnect to adafruit io
      if (! mqtt.connected())
        goto Reconnect;
    }*/


}
