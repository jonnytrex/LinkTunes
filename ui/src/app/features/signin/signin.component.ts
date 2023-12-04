import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgbModal, NgbDatepickerModule } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-signin',
  standalone: true,
  imports: [CommonModule, NgbDatepickerModule],
  templateUrl: './signin.component.html',
  styleUrl: './signin.component.css',
})
export class SigninComponent {
  constructor(private modalService: NgbModal) {}

  public open(modal: any): void {
    this.modalService.open(modal);
  }
}
