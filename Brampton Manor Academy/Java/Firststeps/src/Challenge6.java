public class Challenge6 {
    public static void main(String[] args) {
        int num = Integer.parseInt(args[0]);
        int reversed = 0;
        while (num != 0) {
            int digit = num % 10;
            reversed = reversed * 10 + digit;
            num = num / 10;
        }
        System.out.println(num);
    }
}
