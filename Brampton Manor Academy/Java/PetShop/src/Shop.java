public class Shop {
    public static void main(String[] args) {
        Dog trevor = new Dog("Trevor", "Corgi", 12);
        String name = trevor.getName();
        String breed = trevor.getBreed();
        int age = trevor.getAge();
        System.out.println(name+" "+breed+" "+age);
        trevor.bark();
        trevor.eatBiscuit();
        trevor.getOlder();

        Dog steve = new Dog("Steve", "Shih Tzu", 5);
        String name = steve.getName();
        String breed = steve.getBreed();
        int age = steve.getAge();
        System.out.println(name+" "+breed+" "+age);
        trevor.bark();
        trevor.eatBiscuit();
        trevor.getOlder();

        Dog scooby = new Dog("Scooby", "Great Dane", 7);
        String name = scooby.getName();
        String breed = scooby.getBreed();
        int age = scooby.getAge();
        System.out.println(name+" "+breed+" "+age);
        trevor.bark();
        trevor.eatBiscuit();
        trevor.getOlder();

        Dog brian = new Dog("Brian", "Labrador", 10);
        String name = scooby.getName();
        String breed = scooby.getBreed();
        int age = scooby.getAge();
        System.out.println(name+" "+breed+" "+age);
        trevor.bark();
        trevor.eatBiscuit();
        trevor.getOlder();
    }
}

