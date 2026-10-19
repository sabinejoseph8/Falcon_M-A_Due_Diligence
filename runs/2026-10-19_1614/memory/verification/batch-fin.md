# Verification batch: fin

64 findings. Full cards: see the analyst reports in memory/analyst-reports/ (iteration-1_*.md; FIN-049 to FIN-073 in iteration-2_financial-analyst.md) and X- cards in memory/findings.md.

| ID | Finding (claim) | Workstream | Severity | Confidence | Source(s) | Status |
|---|---|---|---|---|---|---|
| FIN-001 | Q4 2025 revenue spike; underlying FY2025 growth about 8.3% to 8.9% (trend estimate) | Financial | High | Medium | revenue_quarterly.csv; income_statement.csv. Supports X-001 | Open |
| FIN-002 | H1 2026 revenue -0.9%; Q2 -3.0% | Financial | High | High | revenue_quarterly.csv; income_statement.csv. Supports SEC-037, X-002 | Open |
| FIN-003 | Biopharma and informatics growth slowing before 2026; biopharma still +2.7% in H1 2026 | Financial | Medium | High | income_statement.csv rows 2-4 | Open |
| FIN-004 | Gross margin fell 5.0 points in H1 2026 | Financial | High | High | income_statement.csv rows 5-7. Supports SEC-038, X-002 | Open |
| FIN-005 | Reported EBITDA -49.7% in H1 2026 vs Adj. EBITDA -3.4% | Financial | High | High | adjusted_ebitda_reconciliation.csv rows 7, 11. Supports X-002 | Open |
| FIN-006 | Add-backs 30.2% of FY2025 and 44.8% of LTM Adj. EBITDA; Scenario B FY2025 106.4 | Financial | Critical | Medium | adjusted_ebitda_reconciliation.csv rows 7-17. Supports X-015 | Open |
| FIN-007 | Payer denial write-offs (US$10.6m FY2025) are an operating cost added back | Financial | High | High | adjusted_ebitda_reconciliation.csv row 12; kpis.csv row 6. Supports X-015 | Open |
| FIN-008 | Billing system transition costs added back five years running | Financial | Medium | High | adjusted_ebitda_reconciliation.csv row 13. Supports X-015 | Open |
| FIN-009 | Lab start-up costs added back every year, including years with no new labs | Financial | Medium | High | adjusted_ebitda_reconciliation.csv row 14; kpis.csv row 12. Supports X-015 | Open |
| FIN-010 | Legal and regulatory costs up about elevenfold since FY2022 (H1 2026 US$4.8m) | Financial | Medium | Medium | adjusted_ebitda_reconciliation.csv row 15. Related: X-005 | Open |
| FIN-011 | Restructuring charges recur every year | Financial | Medium | High | income_statement.csv row 10; reconciliation row 9 | Open |
| FIN-012 | Cyber incident costs US$6.1m in H1 2026; first-time add-back looks reasonable | Financial | Low | Medium | reconciliation row 16. Supports X-008 | Open |
| FIN-013 | Transaction costs correctly excluded (neutralized) | Financial | Low | High | reconciliation row 17 | Open |
| FIN-015 | Sale-leaseback gain kept out of EBITDA | Financial | Low | High | reconciliation rows 2-7. Supports SEC-029 | Open |
| FIN-016 | LTM Adj. EBITDA at closing may fall below US$110.0m (run-rate 108.2, projection) | Financial | Critical | Medium | reconciliation row 11; revenue_quarterly.csv; deal brief s.3. Supports X-003 | Open |
| FIN-017 | Term loan is 6.1x to 7.4x current or normalized Adj. EBITDA | Financial | High | High | reconciliation; balance_sheet.csv; cash_flow.csv | Open |
| FIN-018 | FY2026 guidance of 137.0 needs H2 53% above H1 | Financial | High | Medium | reconciliation row 11; deal brief s.6. Supports X-002 | Open |
| FIN-019 | Net debt / LTM EBITDA 5.81x; EBITDA / interest 1.11x in H1 2026 | Financial | High | Medium | balance_sheet.csv; reconciliation; income_statement.csv. Supports X-017 | Open |
| FIN-020 | Brief's net debt (391.0) and repayment (424.7) reconcile | Financial | Low | High | balance_sheet.csv rows 2, 16, 17. Supports SEC-011 | Open |
| FIN-021 | Possible debt-like items outside net debt (lease, acquisition) | Financial | Medium | Low | balance_sheet.csv rows 10, 18; cash_flow.csv rows 10, 11 | Open |
| FIN-022 | Liquidity relies on revolver draws; FCF negative | Financial | Medium | Medium | cash_flow.csv; balance_sheet.csv | Open |
| FIN-023 | OCF / Adj. EBITDA fell to 22.7% (FY2025) and 14.4% (H1 2026); FCF negative | Financial | High | High | cash_flow.csv; reconciliation. Supports X-002 | Open |
| FIN-024 | DSO jumped from 62.7 to 79.0 days in FY2025 | Financial | High | High | balance_sheet.csv; income_statement.csv. Related: X-001, X-014; confirms NEWS-015 | Open |
| FIN-025 | Price concession reserve rising more slowly than denials | Financial | High | Medium | balance_sheet.csv rows 22-23; kpis.csv row 6. Supports X-014 | Open |
| FIN-026 | Contract assets growing faster than biopharma revenue | Financial | Medium | Medium | balance_sheet.csv row 4; income_statement.csv row 3 | Open |
| FIN-028 | Net working capital more than doubled; peg needed | Financial | Medium | High | balance_sheet.csv rows 3-6, 12-14 | Open |
| FIN-030 | Medicare FFS rank 1, US$104.3m, 24.2% | Financial | Medium | High | revenue_by_customer.csv row 2. Supports SEC-018 | Open |
| FIN-031 | Veltrane rank 2, US$50.5m, 11.7%; biopharma ex-Veltrane -7.1% | Financial | High | Medium | revenue_by_customer.csv row 3. Supports X-011 | Open |
| FIN-032 | Orvia Health Plan rank 3, US$48.7m, 11.3% | Financial | Medium | High | revenue_by_customer.csv row 4. Related: SEC-022 | Open |
| FIN-034 | Genaro Biosciences is not a listed top 10 customer | Financial | Low | High | revenue_by_customer.csv | Open |
| FIN-036 | Clinical volume (-4.8%) and price per accession (-2.6%) falling in H1 2026 | Financial | High | Medium | kpis.csv rows 2, 3. Supports X-002 | Open |
| FIN-037 | Denial rate nearly doubled since FY2023 (8.9% to 16.2%) | Financial | High | High | kpis.csv row 6. Supports SEC-025 | Open |
| FIN-038 | Backlog fell to 231.4; book-to-bill 0.7 | Financial | High | High | kpis.csv rows 7, 8. Supports SEC-024 | Open |
| FIN-040 | Informatics gross revenue retention stable at 95% to 96% (mitigant) | Financial | Low | High | kpis.csv row 10 | Open |
| FIN-042 | Growing dependence on the hereditary cancer panel paid by Medicare (US$76.2m, 17.7% of revenue) | Financial | Medium | High | kpis.csv rows 4, 5; income_statement.csv row 2. Supports X-004 | Open |
| FIN-043 | Implied multiples on current trading 13.4x to 24.2x | Financial | High | High | deal brief; reconciliation; balance_sheet.csv | Open |
| FIN-044 | Goodwill and intangibles 3.9x book equity; test date not in financials (answered by SEC-019) | Financial | Medium | Medium | balance_sheet.csv. Supports X-013 | Open |
| FIN-045 | FY2025 growth includes an acquisition | Financial | Medium | Medium | cash_flow.csv row 10. Supports SEC-021 | Open |
| FIN-046 | Adj. EBITDA drives bonuses and the financing test | Financial | Medium | High | financials README; deal brief s.3. Supports X-016 | Open |
| FIN-047 | Other liabilities fell US$14.6m in H1 2026, unexplained | Financial | Medium | Low | balance_sheet.csv row 18 | Open |
| FIN-049 | Disclosed US$14.2m replaces trend estimate; underlying FY2025 growth 8.0%; supersedes FIN-001 | Financial | High | High | income_statement.csv; revenue_quarterly.csv; 10-K Item 7. Supports X-001 | Open |
| FIN-050 | Normalized Adj. EBITDA FY2025 111.1, LTM Q2 2026 109.2 (below 110.0); no overlap with denial write-offs | Financial | Critical | High | reconciliation rows 11, 12; 10-K Item 7. Supports X-001, X-003 | Open |
| FIN-051 | Normalized FY2025 gross margin fell 0.5 points; Adj. EBITDA margin rose only 0.8 points | Financial | Medium | High | income_statement.csv rows 5, 7; reconciliation row 11. Supports X-001 | Open |
| FIN-052 | Favorable estimate change conflicts with collection data; under unremediated material weakness | Financial | High | Medium | kpis.csv row 6; balance_sheet.csv rows 3, 22, 23; 10-K Item 9A, Note 2; 10-Q Item 4. Supports X-014 | Open |
| FIN-053 | Bonus at 150% on unadjusted figure; about 57% normalized (inference) | Financial | Medium | High | DEF 14A FY2025 annual bonus. Supports X-016 (same fact as SEC-031) | Open |
| FIN-054 | LTM Adj. EBITDA at a Q2 2027 closing below 110.0 in all three scenarios; supersedes FIN-016 | Financial | Critical | Medium | reconciliation row 11; revenue_by_customer.csv row 3; 8-K Item 7.01; deal brief s.3. Supports X-003 | Open |
| FIN-055 | Estimated covenant position Jun 30, 2026: 4.39x vs 4.50x; headroom about US$2.2m (0.11x) | Financial | High | Medium | income_statement.csv row 11; reconciliation rows 5, 8-10; balance_sheet.csv; 10-K Item 7. Supports X-017 | Open |
| FIN-056 | Jun 30, 2026 compliance depended on the Q4 2025 estimate change (5.36x without it) | Financial | High | Medium | As FIN-055; 10-K Item 7, 9A. Supports X-017 | Open |
| FIN-057 | Projected breach of 4.00x at Sep 30, 2026 (central 4.83x), certificate due before signing | Financial | Critical | Medium | income_statement.csv; reconciliation; balance_sheet.csv; cash_flow.csv; 10-K Item 7; 10-Q Liquidity; 8-K Item 7.01. Supports X-017 | Open |
| FIN-058 | 0419U cut removes about US$29.0m a year (US$382.8m, 23.2% of EV at 13.2x) | Financial | Critical | Medium | income_statement.csv row 2; kpis.csv rows 4, 5; 10-K Item 1; news 2026-07-30. Supports X-004 | Open |
| FIN-059 | Genaro 9% royalty about US$11.8m a year before the cut, 9.2 after; US$68.0m past damages claimed | Financial | High | Medium | income_statement.csv; kpis.csv row 4; LIT-002 file 2026-09-25, 2026-10-02. Supports X-009 | Open |
| FIN-060 | Injunction would put US$102.4m to 131.4m of annual OncoTrace revenue at risk inside the closing LTM window | Financial | High | Low | As FIN-059. Supports X-009 | Open |
| FIN-061 | Genaro's US$68.0m does not reconcile with 9% of OncoTrace revenue in the data pack (implies base 755.6 vs 427.9) | Financial | Medium | Medium | income_statement.csv; kpis.csv row 4; LIT-002 file 2026-09-25. Supports X-009 | Open |
| FIN-062 | Veltrane: US$50.5m revenue and US$61.0m backlog at risk; 10.8% to 15.4% of EV | Financial | Critical | Medium | revenue_by_customer.csv row 3; 10-K Item 1; 10-Q; news 2026-08-27. Supports X-011 | Open |
| FIN-063 | Excluding Veltrane, biopharma revenue 48.1 (-7.1%) and backlog 170.4; group growth ex-Veltrane and ex-14.2 = 5.3% | Financial | Medium | Medium | revenue_by_customer.csv row 3; income_statement.csv; 10-Q. Supports X-011 | Open |
| FIN-064 | Guidance cut supersedes base case; implied H2 2026 Adj. EBITDA 48.9 vs normalized H2 2025 55.1 (-11.3%); updates FIN-018 | Financial | High | High | 8-K Items 2.02, 7.01; reconciliation row 11. Supports X-002 | Open |
| FIN-065 | Rebased valuation: central pro forma run-rate EBITDA 54.8 gives US$6.25 per share at 13.2x (projection) | Financial | Critical | Medium | As cited findings; balance_sheet.csv; deal brief s.2. Supports X-019 | Open |
| FIN-066 | Term loan of 750.0 is 7.3x to 13.7x re-based EBITDA; interest cover 0.89x to 1.67x (projection) | Financial | High | Medium | deal brief s.3; FIN-017; FIN-065. Supports X-019 | Open |
| FIN-067 | Related-party rent premium US$1.2m a year; market rent adds 1.2 of EBITDA (US$15.8m at 13.2x) | Financial | Medium | High | DEF 14A related transactions; 10-K Note 12. Supports SEC-030 | Open |
| FIN-068 | Oct 1, 2025 goodwill test assumptions contradicted by later events | Financial | High | Medium | 10-K goodwill; balance_sheet.csv row 8. Supports X-013 | Open |
| FIN-069 | Orvia (rank 3, US$48.7m) change-of-control termination; 10.4% to 14.8% of EV if it terminates | Financial | High | Medium | revenue_by_customer.csv row 4; 10-K Item 1. Supports SEC-022 | Open |
| FIN-070 | Helixor fixes reagent prices and bears tariffs through 2028 (neutralized) | Financial | Low | High | 10-K Item 1 Suppliers. Supports SEC-028 | Open |
| FIN-071 | Hollis dismissed with prejudice (closed) | Financial | Low | High | 10-Q Part II Item 1. Supports LIT-013 | Open |
| FIN-072 | Cyber lost revenue (about 4.0) correctly not added back; 3.9 of insurance limit left | Financial | Low | Medium | 10-Q Cybersecurity; reconciliation row 16. Supports X-008 | Open |
