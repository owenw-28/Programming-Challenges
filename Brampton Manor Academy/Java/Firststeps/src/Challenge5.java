public class Challenge5 {
    public static void main(String[] args) {
        int num1 = Integer.parseInt(args[0]);
        int num2 = Integer.parseInt(args[1]);
        int result = 1;
        while (num2 != 0) {
            result *= num1;
            --num2;
        }
        System.out.println(result);
    }
}
