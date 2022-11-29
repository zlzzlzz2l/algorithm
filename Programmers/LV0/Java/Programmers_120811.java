import java.util.Arrays;

public class Programmers_120811 {
    public static void main(String[] args) {
        Programmers_120811 s = new Programmers_120811();

        int[] array = {9, -1, 0};

        System.out.println(s.solution(array));
    }

    public int solution(int[] array) {
        int answer = 0;
        Arrays.sort(array);

        answer = array[array.length / 2];

        return answer;
    }
}
