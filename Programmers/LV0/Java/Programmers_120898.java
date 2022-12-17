public class Programmers_120898 {
    public static void main(String[] args) {
        Programmers_120898 s = new Programmers_120898();

        String message = "happy birthday!";

        System.out.println(s.solution(message));
    }

    public int solution(String message) {
        return message.length() * 2;
    }
}
