# console_calculator
Python script representing calculator allowing to run basic arithmetic operations in interactive mode (shell).

To run this script you need installed Docker and Git on your Windows, Linux/Unix or macOS machine.

1. Clone the repository with command
   ```shell
   git clone https://github.com/AlexFromMoscow6/console_calculator.git
   ```
2. Go to directory
   ```shell
   cd console_calculator/
   ```
3. Build with Docker
   ```shell
   docker build -t console_calculator .
   ```
4. And then run
   ```shell
   docker run --rm -it console_calculator
   ```
To exit from program just type q.
