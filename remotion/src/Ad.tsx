import React from 'react';
import { Sequence, useCurrentFrame, interpolate, Audio, staticFile } from 'remotion';

// Audio durations in frames (30 fps)
const DURATIONS = {
  hook: 77,
  pain: 280,
  solution: 252,
  cta: 116
};

// Calculate start frames for each section
const START_FRAMES = {
  hook: 0,
  pain: DURATIONS.hook,
  solution: DURATIONS.hook + DURATIONS.pain,
  cta: DURATIONS.hook + DURATIONS.pain + DURATIONS.solution
};

export const Ad: React.FC = () => {
  const frame = useCurrentFrame();

  const fadeIn = (start: number, duration: number) => {
    const opacity = interpolate(frame, [start, start + duration], [0, 1], {
      extrapolateRight: 'clamp',
      extrapolateLeft: 'clamp',
    });
    return opacity;
  };

  const scaleIn = (start: number, duration: number) => {
    const scale = interpolate(frame, [start, start + duration], [0.5, 1], {
      extrapolateRight: 'clamp',
      extrapolateLeft: 'clamp',
    });
    return scale;
  };

  return (
    <div style={{
      width: '100%',
      height: '100%',
      background: 'linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      color: 'white',
      textAlign: 'center',
      fontFamily: 'Arial, sans-serif',
      position: 'relative',
      overflow: 'hidden'
    }}>
      {/* Voiceovers in sequence with actual durations */}
      <Sequence from={START_FRAMES.hook} durationInFrames={DURATIONS.hook}>
        <Audio src={staticFile('hook.mp3')} />
      </Sequence>
      <Sequence from={START_FRAMES.pain} durationInFrames={DURATIONS.pain}>
        <Audio src={staticFile('pain.mp3')} />
      </Sequence>
      <Sequence from={START_FRAMES.solution} durationInFrames={DURATIONS.solution}>
        <Audio src={staticFile('solution.mp3')} />
      </Sequence>
      <Sequence from={START_FRAMES.cta} durationInFrames={DURATIONS.cta}>
        <Audio src={staticFile('cta.mp3')} />
      </Sequence>

      {/* Background Effect */}
      <div style={{
        position: 'absolute',
        width: '100%',
        height: '100%',
        backgroundImage: 'radial-gradient(circle at 50% 50%, rgba(0, 255, 0, 0.1) 0%, transparent 70%)',
        animation: 'pulse 4s infinite'
      }} />

      {/* Hook Section */}
      <Sequence from={START_FRAMES.hook} durationInFrames={DURATIONS.hook}>
        <div style={{
          opacity: fadeIn(START_FRAMES.hook, 30),
          transform: `scale(${scaleIn(START_FRAMES.hook, 30)})`,
          padding: 50
        }}>
          <h1 style={{
            fontSize: 96,
            fontWeight: 'bold',
            color: '#0f0',
            textShadow: '0 0 20px #0f0',
            margin: 0
          }}>
            STOP LOSING MONEY
          </h1>
          <h2 style={{
            fontSize: 48,
            marginTop: 30,
            color: '#fff'
          }}>
            IN TRADING!
          </h2>
        </div>
      </Sequence>

      {/* Pain Section */}
      <Sequence from={START_FRAMES.pain} durationInFrames={DURATIONS.pain}>
        <div style={{
          opacity: fadeIn(START_FRAMES.pain, 30),
          padding: 50
        }}>
          <h2 style={{
            fontSize: 64,
            color: '#ff6b6b'
          }}>
            Tired of guessing and losing?
          </h2>
          <p style={{
            fontSize: 36,
            marginTop: 40,
            color: '#ccc'
          }}>
            Spending hours on chart analysis...
            <br />
            Missing opportunities...
            <br />
            Watching your profits disappear...
          </p>
        </div>
      </Sequence>

      {/* Solution Section */}
      <Sequence from={START_FRAMES.solution} durationInFrames={DURATIONS.solution}>
        <div style={{
          opacity: fadeIn(START_FRAMES.solution, 30),
          padding: 50
        }}>
          <h1 style={{
            fontSize: 72,
            color: '#0f0',
            textShadow: '0 0 15px #0f0'
          }}>
            CrowdWisdom Trading
          </h1>
          <p style={{
            fontSize: 42,
            marginTop: 40,
            color: '#fff',
            lineHeight: 1.6
          }}>
            AI-powered signals give you real-time insights!
            <br />
            Save time!
            <br />
            Maximize profits!
          </p>
        </div>
      </Sequence>

      {/* CTA Section */}
      <Sequence from={START_FRAMES.cta} durationInFrames={DURATIONS.cta}>
        <div style={{
          opacity: fadeIn(START_FRAMES.cta, 30),
          transform: `scale(${scaleIn(START_FRAMES.cta, 30)})`,
          padding: 50
        }}>
          <div style={{
            background: 'linear-gradient(135deg, #0f0 0%, #00cc00 100%)',
            padding: '40px 80px',
            borderRadius: 20,
            boxShadow: '0 0 40px #0f0'
          }}>
            <h1 style={{
              fontSize: 72,
              margin: 0,
              color: '#000',
              fontWeight: 'bold'
            }}>
              GET STARTED TODAY!
            </h1>
          </div>
          <p style={{
            fontSize: 48,
            marginTop: 40,
            color: '#0f0'
          }}>
            crowdwisdomtrading.com
          </p>
        </div>
      </Sequence>
    </div>
  );
};
