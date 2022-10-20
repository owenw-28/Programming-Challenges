public class Lesson3 {
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
        private static float division(int a, int b){
            float answer = a/b;
            return answer;
        }
        public static void main(String[] args){
            String choice = args[0];

            switch (choice){
                case "addition":
                    int firstValue = Integer.parseInt(args[1]);
                    int secondValue = Integer.parseInt(args[2]);
                    int answer = addition(firstValue, secondValue);
                    System.out.println(answer);
                    break;
            }



            int firstValue = Integer.parseInt(args[1]);
            int secondValue = Integer.parseInt(args[2]);
            int answer = addition(firstValue, secondValue);
            System.out.println(answer);

        }
    }

