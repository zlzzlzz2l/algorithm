import java.util.ArrayList;

public class Programmers_120833 {
    public static void main(String[] args) {
        Programmers_120833 s = new Programmers_120833();

        int[] numbers = {1, 3, 5};
        int num1 = 1;
        int num2 = 2;

        System.out.println(s.solution(numbers, num1, num2));
    }

    public ArrayList<Integer> solution(int[] numbers, int num1, int num2) {
        ArrayList<Integer> answer = new ArrayList<>();

        for (int i = num1; i < num2 + 1; i++) {
            answer.add(numbers[i]);
        }

        return answer;
    }
}
