public class Programmers_120814 {
    public static void main(String[] args) {
        Programmers_120814 s = new Programmers_120814();

        int n = 15;

        System.out.println(s.solution(n));
    }

    public int solution(int n) {
        int answer = 0;

        for (int i = 1; i < n + 1; i += 7) {
            answer += 1;
        }

        return answer;
    }
}
