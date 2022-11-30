public class Programmers_120836 {
    public static void main(String[] args) {
        Programmers_120836 s = new Programmers_120836();

        int n = 100;

        System.out.println(s.solution(n));
    }

    public int solution(int n) {
        int answer = 0;

        for (int i = 1; i < n + 1; i++) {
            if (n % i == 0) {
                answer += 1;
            }
        }

        return answer;
    }
}
