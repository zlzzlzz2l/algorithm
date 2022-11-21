import java.util.Arrays;

public class Programmers_120847 {
    public static void main(String[] args) {
        Programmers_120847 s = new Programmers_120847();

        int[] numbers = {1, 2, 3, 4, 5};

        System.out.println(s.solution(numbers));
    }

    public int solution(int[] numbers) {
        int answer = 0;
        int numbers_len = numbers.length;

        Arrays.sort(numbers);
        answer = numbers[numbers_len-1] * numbers[numbers_len-2];

        return answer;
    }
}
