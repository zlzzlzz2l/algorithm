import java.util.ArrayList;

public class Programmers_120854 {
    public static void main(String[] args) {
        Programmers_120854 s = new Programmers_120854();

        String[] strlist = {"We", "are", "the", "world!"};

        System.out.println(s.solution(strlist));
    }

    public ArrayList<Integer> solution(String[] strlist) {
        ArrayList<Integer> answer = new ArrayList<>();

        for (String word : strlist) {
            answer.add(word.length());
        }

        return answer;
    }
}
