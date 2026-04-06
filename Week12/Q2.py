SEVERITY_ORDER = {"LOW": 1, "MEDIUM": 2, "HIGH": 3}


class Finding:
    def __init__(self, host, title, severity, description):
        self.host = host
        self.title = title
        self.severity = severity
        self.description = description

    def __str__(self):
        return f"[{self.severity}] {self.host} - {self.title}"

    def __eq__(self, other):
        if not isinstance(other, Finding):
            return NotImplemented
        return (
            self.host,
            self.title,
            self.severity,
            self.description,
        ) == (
            other.host,
            other.title,
            other.severity,
            other.description,
        )

    def __lt__(self, other):
        if not isinstance(other, Finding):
            return NotImplemented
        return (
            SEVERITY_ORDER[self.severity],
            self.host,
            self.title,
        ) < (
            SEVERITY_ORDER[other.severity],
            other.host,
            other.title,
        )


class Report:
    def __init__(self, team_name, findings=None):
        self.team_name = team_name
        self.findings = list(findings) if findings else []

    def add_finding(self, finding):
        self.findings.append(finding)

    def __len__(self):
        return len(self.findings)

    def __add__(self, other):
        if not isinstance(other, Report):
            return NotImplemented
        merged_name = f"{self.team_name} + {other.team_name}"
        return Report(merged_name, self.findings + other.findings)

    def display(self):
        print(f"  Team: {self.team_name}")
        print(f"  Total findings: {len(self)}")
        if not self.findings:
            print("    (no findings)")
            return
        for finding in self.findings:
            print(f"    {finding}")


if __name__ == "__main__":
    print("=" * 60)
    print("  Q2: DUNDER METHODS")
    print("=" * 60)

    finding_a = Finding(
        "api.0x10.cloud",
        "Server version exposed",
        "MEDIUM",
        "The API sends a version banner in the response headers.",
    )
    finding_b = Finding(
        "ssh.0x10.cloud",
        "Default credentials",
        "HIGH",
        "SSH accepts admin:admin.",
    )
    finding_c = Finding(
        "blog.0x10.cloud",
        "Missing HTTPS",
        "LOW",
        "The blog is served over HTTP only.",
    )
    finding_d = Finding(
        "api.0x10.cloud",
        "Server version exposed",
        "MEDIUM",
        "The API sends a version banner in the response headers.",
    )

    print("\n--- Comparing Findings ---")
    print(f"  finding_a == finding_d: {finding_a == finding_d}")
    print(f"  finding_a == finding_b: {finding_a == finding_b}")

    print("\n--- Sorting Findings (LOW to HIGH) ---")
    sorted_findings = sorted([finding_a, finding_b, finding_c])
    for finding in sorted_findings:
        print(f"  {finding}")

    report_one = Report("CyberHunters")
    report_one.add_finding(finding_a)
    report_one.add_finding(finding_b)

    report_two = Report("BlueTeam")
    report_two.add_finding(finding_c)
    report_two.add_finding(finding_d)

    print("\n--- Report Lengths ---")
    print(f"  {report_one.team_name}: {len(report_one)} findings")
    print(f"  {report_two.team_name}: {len(report_two)} findings")

    print("\n--- Merged Reports ---")
    merged_report = report_one + report_two
    merged_report.display()

    print("\n" + "=" * 60)
