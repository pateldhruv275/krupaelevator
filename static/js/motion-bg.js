/**
 * Krupa Elevator - Kinetic Motion Background & Particles Engine
 * Integrated with particles.js for Hero Viewport & Custom Hoistway Beams for Global Canvas
 * Hardware-accelerated 60fps, responsive, ultra-clear visibility.
 */

(function () {
  'use strict';

  /* ==========================================================================
     1. HERO VIEWPORT PARTICLES (particles.js library integration)
     ========================================================================== */
  function initHeroParticles() {
    var container = document.getElementById('heroParticles');
    if (!container) return;

    if (typeof window.particlesJS !== 'function') {
      // Retry when window loads if script tag is deferred
      window.addEventListener('load', function() {
        if (typeof window.particlesJS === 'function') initHeroParticles();
      });
      return;
    }

    window.particlesJS('heroParticles', {
      particles: {
        number: {
          value: window.innerWidth < 768 ? 28 : 58,
          density: {
            enable: true,
            value_area: 800
          }
        },
        color: {
          value: ['#008f9a', '#e65a0e', '#00d2d3', '#ffffff', '#ff9f43']
        },
        shape: {
          type: 'circle'
        },
        opacity: {
          value: 0.75,
          random: true,
          anim: {
            enable: true,
            speed: 1.2,
            opacity_min: 0.35,
            sync: false
          }
        },
        size: {
          value: 3.5,
          random: true,
          anim: {
            enable: true,
            speed: 1.8,
            size_min: 1.5,
            sync: false
          }
        },
        line_linked: {
          enable: true,
          distance: 140,
          color: '#008f9a',
          opacity: 0.45,
          width: 1.2
        },
        move: {
          enable: true,
          speed: 1.8,
          direction: 'top', // Ascending vertical motion simulating elevator transit
          random: false,
          straight: false,
          out_mode: 'out',
          bounce: false
        }
      },
      interactivity: {
        detect_on: 'window',
        events: {
          onhover: {
            enable: true,
            mode: 'grab'
          },
          onclick: {
            enable: true,
            mode: 'push'
          },
          resize: true
        },
        modes: {
          grab: {
            distance: 160,
            line_linked: {
              opacity: 0.85
            }
          },
          push: {
            particles_nb: 4
          }
        }
      },
      retina_detect: true
    });
  }

  // Run Hero Particles immediately or upon DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHeroParticles);
  } else {
    initHeroParticles();
  }

  /* ==========================================================================
     2. GLOBAL KINETIC HOISTWAY CANVAS ENGINE (krupaMotionCanvas)
     ========================================================================== */
  var canvas = document.getElementById('krupaMotionCanvas');
  if (!canvas) return;

  var ctx = canvas.getContext('2d');
  if (!ctx) return;

  var width = 0;
  var height = 0;
  var dpr = 1;
  var animationFrameId = null;
  var isTabActive = true;

  // Mouse interaction state
  var mouse = {
    x: -1000,
    y: -1000,
    radius: 150
  };

  window.addEventListener('mousemove', function (e) {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });

  window.addEventListener('mouseleave', function () {
    mouse.x = -1000;
    mouse.y = -1000;
  });

  // Kinetic Elevator Particle Definition
  function ElevatorNode(isInitial) {
    this.reset(isInitial);
  }

  ElevatorNode.prototype.reset = function (isInitial) {
    this.x = Math.random() * width;
    this.y = isInitial ? Math.random() * height : height + Math.random() * 40;
    // Upward vertical velocity (elevators ascending)
    this.vy = -(0.55 + Math.random() * 0.95);
    // Slight gentle horizontal drift
    this.vx = (Math.random() - 0.5) * 0.35;
    this.radius = 2.2 + Math.random() * 2.8;
    // Brand color: 65% Krupa Teal (#008F9A), 35% Safety Orange (#E65A0E)
    this.isTeal = Math.random() > 0.35;
    this.color = this.isTeal ? '0, 143, 154' : '230, 90, 14';
    this.alpha = 0.38 + Math.random() * 0.42;
    this.baseAlpha = this.alpha;
    this.pulseSpeed = 0.02 + Math.random() * 0.03;
    this.pulseAngle = Math.random() * Math.PI * 2;
  };

  ElevatorNode.prototype.update = function () {
    this.y += this.vy;
    this.x += this.vx;

    // Pulse alpha subtly
    this.pulseAngle += this.pulseSpeed;
    this.alpha = this.baseAlpha + Math.sin(this.pulseAngle) * 0.12;

    // Mouse proximity interaction
    var dx = mouse.x - this.x;
    var dy = mouse.y - this.y;
    var dist = Math.sqrt(dx * dx + dy * dy);

    if (dist < mouse.radius) {
      var force = (1 - dist / mouse.radius) * 2.2;
      this.x -= (dx / dist) * force;
      this.y -= (dy / dist) * force;
      this.alpha = Math.min(this.baseAlpha + 0.45, 0.95);
    }

    // Recycle when scrolled above screen
    if (this.y < -30 || this.x < -30 || this.x > width + 30) {
      this.reset(false);
    }
  };

  ElevatorNode.prototype.draw = function () {
    var drawAlpha = Math.max(0.15, Math.min(0.95, this.alpha));

    // Outer glow aura
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius * 1.6, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(' + this.color + ', ' + (drawAlpha * 0.25) + ')';
    ctx.fill();

    // Core node
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(' + this.color + ', ' + drawAlpha + ')';
    ctx.fill();

    // Brilliant white center highlight
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius * 0.5, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(255, 255, 255, ' + (drawAlpha * 0.9) + ')';
    ctx.fill();
  };

  // Vertical Guide Rail Beams (Elevator Hoistway Tracks)
  function HoistwayBeam(xRatio) {
    this.xRatio = xRatio;
    this.pulseY = Math.random() * 1200;
    this.speed = 1.4 + Math.random() * 1.8;
    this.beamLength = 160 + Math.random() * 160;
    this.isTeal = Math.random() > 0.4;
    this.color = this.isTeal ? '0, 143, 154' : '230, 90, 14';
  }

  HoistwayBeam.prototype.update = function () {
    this.pulseY -= this.speed;
    if (this.pulseY < -this.beamLength) {
      this.pulseY = height + 100 + Math.random() * 300;
    }
  };

  HoistwayBeam.prototype.draw = function () {
    var x = width * this.xRatio;

    // Faint vertical guide rail line
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, height);
    ctx.strokeStyle = 'rgba(0, 143, 154, 0.18)';
    ctx.lineWidth = 1;
    ctx.stroke();

    // Travelling elevator pulse beam
    var grad = ctx.createLinearGradient(0, this.pulseY, 0, this.pulseY + this.beamLength);
    grad.addColorStop(0, 'rgba(' + this.color + ', 0)');
    grad.addColorStop(0.5, 'rgba(' + this.color + ', 0.65)');
    grad.addColorStop(1, 'rgba(' + this.color + ', 0)');

    ctx.beginPath();
    ctx.moveTo(x, this.pulseY);
    ctx.lineTo(x, this.pulseY + this.beamLength);
    ctx.strokeStyle = grad;
    ctx.lineWidth = 2.5;
    ctx.stroke();

    // Little elevator cab transit beacon on the rail
    var beaconY = this.pulseY + this.beamLength * 0.5;
    ctx.beginPath();
    ctx.arc(x, beaconY, 3.5, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(255, 255, 255, 0.95)';
    ctx.shadowColor = 'rgba(' + this.color + ', 0.8)';
    ctx.shadowBlur = 8;
    ctx.fill();
    ctx.shadowBlur = 0; // reset
  };

  var nodes = [];
  var beams = [];

  function initElements() {
    nodes = [];
    beams = [];

    var isMobile = width < 768;
    var nodeCount = isMobile ? 26 : 54;
    for (var i = 0; i < nodeCount; i++) {
      nodes.push(new ElevatorNode(true));
    }

    // 6 architectural vertical guide rail tracks across viewport
    var beamRatios = isMobile ? [0.18, 0.5, 0.82] : [0.08, 0.22, 0.40, 0.60, 0.78, 0.92];
    beamRatios.forEach(function (ratio) {
      beams.push(new HoistwayBeam(ratio));
    });
  }

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    width = window.innerWidth;
    height = window.innerHeight;

    canvas.width = width * dpr;
    canvas.height = height * dpr;
    canvas.style.width = width + 'px';
    canvas.style.height = height + 'px';

    ctx.scale(dpr, dpr);
    initElements();
  }

  // Draw dynamic interconnected telemetry lines between nearby nodes
  function drawLinks() {
    var maxDist = width < 768 ? 95 : 135;
    var len = nodes.length;

    for (var i = 0; i < len; i++) {
      for (var j = i + 1; j < len; j++) {
        var dx = nodes[i].x - nodes[j].x;
        var dy = nodes[i].y - nodes[j].y;
        var dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < maxDist) {
          var lineAlpha = (1 - dist / maxDist) * 0.35;
          ctx.beginPath();
          ctx.moveTo(nodes[i].x, nodes[i].y);
          ctx.lineTo(nodes[j].x, nodes[j].y);
          ctx.strokeStyle = 'rgba(0, 143, 154, ' + lineAlpha + ')';
          ctx.lineWidth = 1.2;
          ctx.stroke();
        }
      }
    }
  }

  function render() {
    if (!isTabActive) return;

    ctx.clearRect(0, 0, width, height);

    // 1. Draw vertical hoistway guide rail tracks & traveling pulses
    for (var b = 0; b < beams.length; b++) {
      beams[b].update();
      beams[b].draw();
    }

    // 2. Draw telemetry links between nearby nodes
    drawLinks();

    // 3. Update & render ascending elevator nodes
    for (var n = 0; n < nodes.length; n++) {
      nodes[n].update();
      nodes[n].draw();
    }

    animationFrameId = requestAnimationFrame(render);
  }

  // Handle visibility change (pause loop when tab inactive to save battery)
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) {
      isTabActive = false;
      if (animationFrameId) cancelAnimationFrame(animationFrameId);
    } else {
      isTabActive = true;
      render();
    }
  });

  // Debounced resize
  var resizeTimeout;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(function () {
      resize();
    }, 120);
  });

  // Initialize
  resize();
  render();
  console.log('[Krupa Elevator] Kinetic Motion Background Engine running at 60fps');
})();
