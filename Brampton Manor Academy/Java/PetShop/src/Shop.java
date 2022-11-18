public class Shop {
    public static void main(String[] args) {
        Dog trevor = new Dog("Trevor", "Corgi", 12);
        String name1 = trevor.getName();
        String breed1 = trevor.getBreed();
        int age1 = trevor.getAge();
        System.out.println(name1+" "+breed1+" "+age1);
        trevor.bark();
        trevor.eatBiscuit();
        trevor.getOlder();
        System.out.println("");

        Dog steve = new Dog("Steve", "Shih Tzu", 5);
        String name2 = steve.getName();
        String breed2 = steve.getBreed();
        int age2 = steve.getAge();
        System.out.println(name2+" "+breed2+" "+age2);
        steve.bark();
        steve.eatBiscuit();
        steve.getOlder();
        System.out.println("");

        Dog scooby = new Dog("Scooby", "Great Dane", 7);
        String name3 = scooby.getName();
        String breed3 = scooby.getBreed();
        int age3 = scooby.getAge();
        System.out.println(name3+" "+breed3+" "+age3);
        scooby.bark();
        scooby.eatBiscuit();
        scooby.getOlder();
        System.out.println("");

        Dog brian = new Dog("Brian", "Labrador", 10);
        String name4 = brian.getName();
        String breed4 = brian.getBreed();
        int age4 = brian.getAge();
        System.out.println(name4+" "+breed4+" "+age4);
        brian.bark();
        brian.eatBiscuit();
        brian.getOlder();
        System.out.println("");
    }
}

