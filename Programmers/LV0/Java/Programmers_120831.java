public class Programmers_120831 {
    public static void main(String[] args) {
        Programmers_120831 s = new Programmers_120831();

        int n = 10;

        System.out.println(s.solution(n));
    }

    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i < n + 1; i++) {
            if (i % 2 == 0) {
                answer += i;
            }
        }
        return answer;
    }
}
