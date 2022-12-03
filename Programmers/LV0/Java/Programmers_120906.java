public class Programmers_120906 {
    public static void main(String[] args) {
        Programmers_120906 s = new Programmers_120906();

        int n = 1234;

        System.out.println(s.solution(n));
    }

    public int solution(int n) {
        int answer = 0;
        String str_num = String.valueOf(n);
        String[] str_n = str_num.split("");

        for (String s : str_n) {
            answer += Integer.parseInt(s);
        }

        return answer;
    }
}
