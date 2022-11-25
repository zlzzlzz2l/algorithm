public class Programmers_120841 {
    public static void main(String[] args) {
        Programmers_120841 s = new Programmers_120841();

        int[] dot = {-7, 4};

        System.out.println(s.solution(dot));
    }

    public int solution(int[] dot) {
        int answer = 0;

        if (dot[0] > 0 && dot[1] > 0) {
            answer = 1;
        } else if (dot[0] > 0 && dot[1] < 0) {
            answer = 4;
        } else if (dot[0] < 0 && dot[1] < 0) {
            answer = 3;
        } else answer = 2;

        return answer;
    }
}
