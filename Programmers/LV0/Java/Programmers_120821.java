import java.util.ArrayList;

public class Programmers_120821 {
    public static void main(String[] args) {
        Programmers_120821 s = new Programmers_120821();

        int[] num_list = {1, 2, 3, 4, 5};

        System.out.println(s.solution(num_list));
    }

    public ArrayList<Integer> solution(int[] num_list) {
        ArrayList<Integer> answer = new ArrayList<>();

        int num_list_len = num_list.length;
        for (int i = num_list_len; i > 0; i--) {
            answer.add(num_list[i-1]);
        }

        return answer;
    }
}
