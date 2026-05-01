import { Composition, registerRoot } from 'remotion';
import { Ad } from './Ad';

// Total duration of all sections (77 + 280 + 252 + 116 = 725 frames)
const TOTAL_DURATION = 725;

const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="Ad"
        component={Ad}
        durationInFrames={TOTAL_DURATION}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};

registerRoot(RemotionRoot);
