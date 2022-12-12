import java.util.ArrayList;
import java.util.List;

public class Programmers_120849 {
    public static void main(String[] args) {
        Programmers_120849 s = new Programmers_120849();

        String my_string = "bus";

        System.out.println(s.solution(my_string));
    }

    public String solution(String my_string) {
        String answer = "";

        String[] vowels = {"a", "e", "i", "o", "u"};
        String[] myStr = my_string.split("");

        for (String s : myStr) {
            int compare = 0;

            for (String vowel : vowels) {
                if (s.equals(vowel)) {
                    compare += 1;
                }
            }
            if (compare == 0) {
                answer += s;
            }
        }

        return answer;
    }
}
