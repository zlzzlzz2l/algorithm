public class Programmers_120909 {
    public static void main(String[] args) {
        Programmers_120909 s = new Programmers_120909();

        int n = 999;

        System.out.println(s.solution(n));
    }

    public int solution(int n) {
        int answer = 2;

        for (int i = 1; i < n+1; i++) {
            if (n == i*i) {
                answer = 1;
                break;
            }
        }

        return answer;
    }
}
