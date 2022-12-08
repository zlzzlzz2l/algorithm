public class Programmers_120826 {
    public static void main(String[] args) {
        Programmers_120826 s = new Programmers_120826();

        String my_string = new String("abcdef");
        String letter = "f";

        System.out.println(s.solution(my_string, letter));
    }

    public String solution(String my_string, String letter) {
        StringBuilder answer = new StringBuilder();

        String[] my_str = my_string.split("");

        for (String s : my_str) {
            if (s.equals(letter)) {
                continue;
            } else {
                answer.append(s);
            }
        }

        return answer.toString();
    }
}
