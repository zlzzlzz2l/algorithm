import java.util.Arrays;

public class Programmers_120889 {
    public static void main(String[] args) {
        Programmers_120889 s = new Programmers_120889();

        int[] sides = {199, 72, 222};

        System.out.println(s.solution(sides));
    }

    public int solution(int[] sides) {
        int answer = 2;
        Arrays.sort(sides);

        if (sides[2] < sides[0] + sides[1]) {
            answer = 1;
        }

        return answer;
    }
}
