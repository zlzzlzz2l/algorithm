import java.util.ArrayList;

public class Programmers_120813 {
    public static void main(String[] args) {
        Programmers_120813 s = new Programmers_120813();

        int n = 10;

        System.out.println(s.solution(n));
    }

    public ArrayList<Integer> solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();

        for (int i = 1; i < n + 1; i++) {
            if (i % 2 == 0) {
                continue;
            }
            answer.add(i);
        }

        return answer;
    }
}
