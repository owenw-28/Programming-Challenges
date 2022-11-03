public class Calculator {
    private static int addition(int a, int b){
        int answer = a + b;
        return answer;
    }
    private static int subtraction(int a, int b){
        int answer = a - b;
        return answer;
    }
    private static int multiplication(int a, int b){
        int answer = a * b;
        return answer;
    }
    private static int division(int a, int b){
        int answer = a/b;
        return answer;
    }
    private static int square(int base_square){
        int answer = base_square * base_square;
        return answer;
    }
    private static int cube(int base_cube){
        int answer = base_cube * base_cube * base_cube;
        return answer;
    }
    private static int power_of(int base_power_of, int exponent){
        int total = 0;
        for (int i = 0; i < exponent; i++){
            total = total + (base_power_of * base_power_of);
        }
        return total;
    }

    private static int factorial(int num) {
        int i, fact = 1;
        for (i = 1; i <= num; i++) {
            fact = fact * i;
        }
        return fact;
    }


        public static void main(String[] args){
        String choice = args[0];

        switch (choice){
            case "addition":
                int add1 = Integer.parseInt(args[1]);
                int add2 = Integer.parseInt(args[2]);
                int answer = addition(add1, add2);
                System.out.println(answer);
                break;
            case "subtraction":
                int subtract1 = Integer.parseInt(args[1]);
                int subtract2 = Integer.parseInt(args[2]);
                int answer1 = subtraction(subtract1, subtract2);
                System.out.println(answer1);
                break;
            case "multiplication":
                int multiply1 = Integer.parseInt(args[1]);
                int multiply2 = Integer.parseInt(args[2]);
                int answer2 = multiplication(multiply1, multiply2);
                System.out.println(answer2);
                break;
            case "division":
                int divide1 = Integer.parseInt(args[1]);
                int divide2 = Integer.parseInt(args[2]);
                int answer3 = division(divide1, divide2);
                System.out.println(answer3);
                break;
            case "square":
                int base_square = Integer.parseInt(args[1]);
                int answer4 = square(base_square);
                System.out.println(answer4);
                break;
            case "cube":
                int base_cube = Integer.parseInt(args[1]);
                int answer5 = cube(base_cube);
                System.out.println(answer5);
                break;
            case "power":
                int base_power_of = Integer.parseInt(args[1]);
                int exponent = Integer.parseInt(args[2]);
                int answer6 = power_of(base_power_of, exponent);
                System.out.println(answer6);
                break;
            case "factorial":
                int num = Integer.parseInt(args[1]);
                int answer7 = factorial(num);
                System.out.println(answer7);
                break;
        }


    }
}
