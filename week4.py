def calculate_tickets_value(ticket_type, tickets_resolved, priority_level):
    if ticket_type == "technical":
        if priority_level == "low":
            total = 20 * tickets_resolved
        elif priority_level == "medium":
            total = 35 * tickets_resolved
        elif priority_level == "high":
            total = 55 * tickets_resolved
    elif ticket_type == "billing":
        if priority_level == "low":
            total = 15 * tickets_resolved
        elif priority_level == "medium":
            total = 25 * tickets_resolved
        elif priority_level == "high":
            total = 40 * tickets_resolved
    elif ticket_type == "general":
        if priority_level == "low":
            total = 10 * tickets_resolved
        elif priority_level == "medium":
            total = 18 * tickets_resolved
        elif priority_level == "high":
            total = 28 * tickets_resolved
    return total


def calculate_resolution_efficiency(agent_quarters, baseline_tickets, resolved_tickets):
    expected_tickets = 1000 + (agent_quarters * 100)
    ticket_capacity = expected_tickets - baseline_tickets
    efficiency_percentage = (resolved_tickets - baseline_tickets) / ticket_capacity * 100
    return round(efficiency_percentage, 1)


def determine_performance_level(efficiency_percent):
    if efficiency_percent < 50:
        level = "Developing Level"
    elif efficiency_percent < 60:
        level = "Competent Level"
    elif efficiency_percent < 70:
        level = "Proficient Level"
    elif efficiency_percent < 85:
        level = "Advanced Level"
    else:
        level = "Expert Level"
    return level


def calculate_performance_bonus(value, tickets, level_multiplier):
    base_bonus = value * 0.05 + tickets * 2
   
    if level_multiplier == "Developing Level":
        final_bonus = base_bonus * 0.5
    elif level_multiplier == "Competent Level":
        final_bonus = base_bonus * 1.0
    elif level_multiplier == "Proficient Level":
        final_bonus = base_bonus * 1.2
    elif level_multiplier == "Advanced Level":
        final_bonus = base_bonus * 1.5
    elif level_multiplier == "Expert Level":
        final_bonus = base_bonus * 1.8
    return round(final_bonus, 1)


def needs_additional_training(service_weeks, total_tickets, avg_efficiency):
    if service_weeks >= 6 and avg_efficiency < 50:
        return True
    if total_tickets < 100 and avg_efficiency < 60:
        return True
    if service_weeks >= 4 and avg_efficiency < 40:
        return True
    return False


def generate_quality_report(agent_name, ticket_type, tickets, priority_level, agent_quarters, baseline_tickets, resolved_tickets, service_weeks):
    value = calculate_tickets_value(ticket_type, tickets, priority_level)
    efficiency = calculate_resolution_efficiency(agent_quarters, baseline_tickets, resolved_tickets)
    level = determine_performance_level(efficiency)
    bonus = calculate_performance_bonus(value, tickets, level)
    training_needed = needs_additional_training(service_weeks, tickets, efficiency)

    print("CUSTOMER SERVICE QUALITY MONITOR")
    print("========================================")
    print(f"Quality Report for: {agent_name}")
    print("----------------------------------------")
    print(f"Ticket Type: {ticket_type}")
    print(f"Tickets Resolved: {tickets}")
    print(f"Priority Level: {priority_level}")
    print(f"Tickets Value: ${value}")
    print("Efficiency Analysis:")
    print(f"  Experience: {agent_quarters} quarters, Baseline: {baseline_tickets}, Resolved Tickets: {resolved_tickets}")
    print(f"  Efficiency: {efficiency}%")
    print(f"  Performance Level: {level}")
    print(f"Performance Bonus: ${bonus}")
    print(f"Service Weeks: {service_weeks}")
    print(f"Additional Training Needed: {'Yes' if training_needed else 'No'}")
    print()



generate_quality_report("Harper", "technical", 45, "high", 3, 800, 1150, 3)
generate_quality_report("Indigo", "billing", 60, "medium", 5, 900, 1300, 5)
generate_quality_report("Jesse", "general", 30, "low", 8, 850, 950, 7)