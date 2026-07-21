function PredictionCard({ prediction, confidence }) {
    if (!prediction) return null;

    const conf = Math.round(Number(confidence) || 0);
    const pct = Math.min(100, Math.max(0, conf));
    const positive = String(prediction).toLowerCase().includes('posit');
    const barStyle = {
        width: `${pct}%`,
        boxShadow: `0 8px 24px rgba(0,180,255,${Math.min(pct / 150, 0.45)})`,
        transition: 'width 600ms ease, box-shadow 600ms ease'
    };

    return (
        <div className="mt-6 bg-gradient-to-b from-slate-900/60 to-slate-900/40 border border-slate-700 rounded-xl shadow-2xl p-6 text-slate-100">
            <div className="flex items-center justify-between">
                <h2 className="text-lg font-semibold">Prediction</h2>
                <div className="text-sm text-slate-400">Confidence</div>
            </div>

            <div className="mt-4 flex items-center gap-4">
                <div className="text-3xl">{positive ? '😊' : '😞'}</div>
                <div className="flex-1">
                    <div className="flex items-baseline justify-between">
                        <p className="text-xl font-bold">{positive ? 'Positive' : 'Negative'}</p>
                        <div className="text-sm text-slate-300 font-mono">{pct}%</div>
                    </div>

                    <div className="mt-3 h-3 w-full bg-slate-800 rounded-full overflow-hidden border border-slate-700">
                        <div style={barStyle} className="h-full bg-gradient-to-r from-[#00b4ff] to-[#0066ff]" />
                    </div>
                </div>
            </div>
        </div>
    );
}

export default PredictionCard;