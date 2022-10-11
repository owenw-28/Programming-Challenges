public class Lesson2 {
    public static void main(String[] args) {
        for_loop();
        cars_list();
        daysofweekif();
        daysofweekswitch();
        catching();
    }
    public static void for_loop(){
        for (int i = 0; i < 5; i++){
            System.out.println("Yes");
        }
    }

    public static void cars_list(){
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        for (int i=0; i < cars.length; i++){
            System.out.println(cars[i]);
        }
    }
    public static void daysofweekif(){
        int day = 4;
        if (day==1){
            System.out.println("Today is Monday");
        } else if (day==2){
            System.out.println("Today is Tuesday");
        } else if (day==3){
            System.out.println("Today is Wednesday");
        } else if (day==4){
            System.out.println("Today is Thursday");
        } else if (day==5) {
            System.out.println("Today is Friday");
        } else if (day==6) {
            System.out.println("Today is Saturday");
        } else if (day==5) {
            System.out.println("Today is Sunday");
        }
    }
    public static void daysofweekswitch(){
        int day = 4;
        switch(day) {
            case 1:
                System.out.println("Today is Monday");
                break;
            case 2:
                System.out.println("Today is Tuesday");
                break;
            case 3:
                System.out.println("Today is Wednesday");
                break;
            case 4:
                System.out.println("Today is Thursday");
                break;
            case 5:
                System.out.println("Today is Friday");
                break;
            case 6:
                System.out.println("Today is Saturday");
                break;
            case 7:
                System.out.println("Today is Sunday");
                break;
        }
    }
    public static void catching(){
        int[] myNumbers = {1, 2, 3};
        try {
            System.out.println(myNumbers[10]);
        } catch (Exception e) {
            System.out.println("Array index out of bounds");
        }
    }
}
