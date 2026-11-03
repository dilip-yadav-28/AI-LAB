import random
import math
N = 8  
def get_cost(state):
    """Calculates number of mutually attacking pairs of queens."""
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts
def simulated_annealing():
   
    current_state = [random.randint(0, N - 1) for _ in range(N)]
    current_cost = get_cost(current_state)
   
    T = 100.0          
    cooling_rate = 0.95 
    threshold = 0.01   
    step = 0
    print(f"Initial State: {current_state} | Initial Conflicts: {current_cost}\n")
   
    while T > threshold:
        if current_cost == 0:
            print(f"\n🎉 SUCCESS: Found goal state {current_state} in {step} steps!")
            return True
           
        step += 1
        print(f"\n--- STEP {step} (Current Temp: {T:.2f}) ---")
        print(f"Current State: {current_state} (Cost: {current_cost})")
       
        random_col = random.randint(0, N - 1)
        random_row = random.randint(0, N - 1)
        while random_row == current_state[random_col]:
            random_row = random.randint(0, N - 1)
           
        neighbor_state = list(current_state)
        neighbor_state[random_col] = random_row
        neighbor_cost = get_cost(neighbor_state)

      
        print(f"Generated Neighbor State: {neighbor_state} (Cost: {neighbor_cost})")

     
        delta_E = neighbor_cost - current_cost
        print(f"Delta E (Neighbor Cost - Current Cost): {delta_E}")

      
        if delta_E < 0:
            # Better state -> Always accept
            current_state = neighbor_state
            current_cost = neighbor_cost
            print("Decision: Move ACCEPTED (Neighbor is better).")
        else:
          
            acceptance_prob = math.exp(-delta_E / T)
            random_val = random.random()
            print(f"Acceptance Probability: {acceptance_prob:.4f} | Random Roll: {random_val:.4f}")

            if random_val < acceptance_prob:
                current_state = neighbor_state
                current_cost = neighbor_cost
                print(" Decision: Move ACCEPTED (Worse state accepted to escape local minimum trap).")
            else:
                print("Decision: Move REJECTED. Staying at current state.")

    
        T *= cooling_rate

    print(f"\nTIMEOUT: Reached freezing point. Final state found: {current_state} with cost {current_cost}")
    return current_cost == 0


success = False
attempt = 1
while not success:
    print(f"=== RUN ATTEMPT {attempt} ===")
    success = simulated_annealing()
    attempt += 1
    print("\n" + "="*50 + "\n")