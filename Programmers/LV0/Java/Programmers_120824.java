import java.util.ArrayList;

public class Programmers_120824 {
    public static void main(String[] args) {
        Programmers_120824 s = new Programmers_120824();

        int[] num_list = {1, 2, 3, 4, 5};

        System.out.println(s.solution(num_list));
    }

    public ArrayList<Integer> solution(int[] num_list) {
        ArrayList<Integer> answer = new ArrayList<>();

        int even = 0;
        int odd = 0;

        for (int num : num_list) {
            if (num % 2 == 0) {
                even += 1;
            } else odd += 1;
        }

        answer.add(even);
        answer.add(odd);

        return answer;
    }
}
