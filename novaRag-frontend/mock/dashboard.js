export default {
  kpis: {
    discoveredApis: 3,
    attackSessions: 6,
    criticalFindings: 1,
    avgResponseTimeSeconds: 0.0092
  },

  severityBreakdown: {
    Critical: 1,
    High: 1,
    Medium: 1,
    Low: 3
  },

  attackTimeline: [
    { time: "09:15", count: 1 },
    { time: "09:20", count: 1 },
    { time: "09:26", count: 1 },
    { time: "09:30", count: 1 },
    { time: "09:35", count: 1 },
    { time: "09:38", count: 1 },
    { time: "09:41", count: 1 }
  ],

  responseTimeSeries: [
    { time: "09:15", seconds: 0.004 },
    { time: "09:20", seconds: 0.007 },
    { time: "09:26", seconds: 0.009 },
    { time: "09:30", seconds: 0.014 },
    { time: "09:35", seconds: 0.006 },
    { time: "09:38", seconds: 0.011 },
    { time: "09:41", seconds: 0.008 }
  ]
}