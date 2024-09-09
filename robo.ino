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
      // Mover para a esquerda suavemente
      digitalWrite(dir1, LOW);  // Direção esquerda
      digitalWrite(dir2, HIGH); // Direção direita
      analogWrite(motor1, 150); // Reduz velocidade do motor esquerdo
      analogWrite(motor2, 200); // Velocidade normal no motor direito
    } 
    else if (command == 'R') {
      // Mover para a direita suavemente
      digitalWrite(dir1, HIGH); // Direção esquerda
      digitalWrite(dir2, LOW);  // Direção direita
      analogWrite(motor1, 200); // Velocidade normal no motor esquerdo
      analogWrite(motor2, 150); // Reduz velocidade do motor direito
    } 
    else if (command == 'F') {
      // Mover para frente (bola centralizada)
      digitalWrite(dir1, HIGH); // Ambos os motores para frente
      digitalWrite(dir2, HIGH);
      analogWrite(motor1, 200); // Velocidade normal
      analogWrite(motor2, 200);
    } 
    else if (command == 'S') {
      // Parar os motores
      analogWrite(motor1, 0);
      analogWrite(motor2, 0);
    } 
    else if (command == 'N') {
      // Caso não veja a bola, parar o robô
      analogWrite(motor1, 0);
      analogWrite(motor2, 0);
    }
  }
}
