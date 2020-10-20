import java.io.*;
import java.util.Scanner;

class Main {

    static double frontLeftMotor, frontRightMotor, backLeftMotor, backRightMotor;
    static double[] speed = {frontLeftMotor, frontRightMotor, backLeftMotor, backRightMotor};
    static Scanner scanner = new Scanner(new InputStreamReader(System.in));
    static String[] motors = {"frontLeftMotor", "frontRightMotor", "backLeftMotor", "backRightMotor"};

    public static void main(String[] args) {
        setSpeed();
        for (int i = 0; i < motors.length; i++){
            System.out.println(motors[i] + ": " + speed[i]);
        }
    }

    static void setSpeed(){

        for (int i = 0; i < motors.length; i++){
            while (true){
                System.out.println("Please set the value of " + motors[i]);
                double input = scanner.nextDouble();
                System.out.println("The input is " + input);
                if (-1.0 <= input && 1.0 >= input){
                    speed[i] = input;
                    break;
                }else{
                    System.out.println("This speed is not valid");
                }

            }   
        }
    }
}