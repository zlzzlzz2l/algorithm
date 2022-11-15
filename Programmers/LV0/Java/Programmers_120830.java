public class Programmers_120830 {
    public static void main(String[] args) {
        Programmers_120830 s = new Programmers_120830();

        int n = 10;
        int k = 3;

        System.out.println(s.solution(n, k));
    }

    public int solution(int n, int k) {
        int answer = 0;
        int check = n / 10;

        answer = (12000 * n) + (2000 * (k-check));

        return answer;
    }
}
