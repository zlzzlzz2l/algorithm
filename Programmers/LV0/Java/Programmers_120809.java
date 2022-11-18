import java.util.ArrayList;

public class Programmers_120809 {
    public static void main(String[] args) {
        Programmers_120809 s = new Programmers_120809();

        int[] numbers = {1, 2, 3, 4, 5};

        System.out.println(s.solution(numbers));
    }

    public ArrayList<Integer> solution(int[] numbers) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int num : numbers) {
            answer.add(num * 2);
        }
        return answer;
    }
}
