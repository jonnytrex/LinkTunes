import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { NgbDatepicker, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { NgxAudioPlayerModule, Track } from 'ngx-audio-player';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, NgbDatepicker, NgxAudioPlayerModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent {
  mssapDisplayTitle = true;
  mssapDisablePositionSlider = true;
  mssapDisplayRepeatControls = true;
  mssapDisplayVolumeControls = true;
  mssapDisplayVolumeSlider = false;

  // Material Style Simple Audio Player
  mssapPlaylist: Track[] = [
    {
      title: 'Strange',
      link: '../../../assets/Strange.mp3',
      artist: 'Galaxie 500',
      duration: 180,
    },
  ];
}
