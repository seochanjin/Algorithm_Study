import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;

        Map<String, Integer> wantMap = new HashMap<>();
        Map<String, Integer> discountMap = new HashMap<>();

        for(int i = 0; i < want.length; i++){
            wantMap.put(want[i], number[i]);
        }

        for(int i = 0; i < 10; i++){
            discountMap.put(
                    discount[i],
                    discountMap.getOrDefault(discount[i], 0) + 1);
        }

        if (discountMap.equals(wantMap)){
            answer++;
        }


        for(int i = 10; i < discount.length; i++){
            discountMap.put(
                    discount[i],
                    discountMap.getOrDefault(discount[i], 0) + 1);

            String removeItem = discount[i - 10];

            discountMap.put(
                    removeItem,
                    discountMap.get(removeItem) - 1);

            if (discountMap.get(removeItem) == 0) {
                discountMap.remove(removeItem);
            }

            if (discountMap.equals(wantMap)) {
                answer++;
            }

        }

        return answer;
    }
}