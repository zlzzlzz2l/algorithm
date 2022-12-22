import java.util.ArrayList;

public class Programmers_120905 {
    public static void main(String[] args) {
        Programmers_120905 s = new Programmers_120905();

        int n = 3;
        int[] numlist = {4, 5, 6, 7, 8, 9, 10, 11, 12};

        System.out.println(s.solution(n, numlist));
    }

    public ArrayList<Integer> solution(int n, int[] numlist) {
        ArrayList<Integer> answer = new ArrayList<>();

        for (int num : numlist) {
            if (num % n == 0) answer.add(num);
        }

        return answer;
    }
}
