import java.util.ArrayList;

public class Programmers_120903 {
    public static void main(String[] args) {
        Programmers_120903 s = new Programmers_120903();

        String[] s1 = {"a", "b", "c"};
        String[] s2 = {"com", "b", "d", "p", "c"};

        System.out.println(s.solution(s1, s2));
    }

    public int solution(String[] s1, String[] s2) {
        int answer = 0;

        if (s1.length > s2.length) {
            for (String s : s2) {
                for (String value : s1) {
                    if (value.equals(s)) {
                        answer += 1;
                    }
                }
            }
        } else {
            for (String s : s1) {
                for (String value : s2) {
                    if (s.equals(value)) {
                        answer += 1;
                    }
                }
            }
        }

        return answer;
    }
}
