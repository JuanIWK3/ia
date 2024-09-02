const int motor1 = 5; // velocidade motor 1
const int motor2 = 6; // velocidade motor 2
const int dir1 = 7;   // direção do motor 1
const int dir2 = 8;   // direção do motor 2

void setup() {
  pinMode(motor1, OUTPUT);
  pinMode(motor2, OUTPUT);
  pinMode(dir1, OUTPUT);
  pinMode(dir2, OUTPUT);
  
  Serial.begin(9600); // Inicializa a comunicação serial
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Lê o comando recebido

    if (command == 'L') {
      // Mover para a esquerda
      digitalWrite(dir1, LOW);
      digitalWrite(dir2, HIGH);
      analogWrite(motor1, 200);
      analogWrite(motor2, 200);
    } else if (command == 'R') {
      // Mover para a direita
      digitalWrite(dir1, HIGH);
      digitalWrite(dir2, LOW);
      analogWrite(motor1, 200);
      analogWrite(motor2, 200);
    } else if (command == 'S') {
      // Parar os motores
      analogWrite(motor1, 0);
      analogWrite(motor2, 0);
    }
  }
}
