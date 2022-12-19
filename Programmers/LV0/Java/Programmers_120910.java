public class Programmers_120910 {
    public static void main(String[] args) {
        Programmers_120910 s = new Programmers_120910();

        int n = 7;
        int t = 15;

        System.out.println(s.solution(n, t));
    }

    public int solution(int n, int t) {
        int answer = n;

        for (int i = 1; i < t + 1; i++) {
            answer *= 2;
        }

        return answer;
    }
}
