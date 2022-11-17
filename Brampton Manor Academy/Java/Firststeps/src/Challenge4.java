public class Challenge4 {
    public static void main(String[] args) {
        int num = Integer.parseInt(args[0]);
            int i, fact = 1;
            for (i = 1; i <= num; i++) {
                fact = fact * i;
            }
        System.out.println(fact);
        }
    }

